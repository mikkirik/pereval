from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin, NestedUpdateMixin
from .models import User, Coords, Image, Level, Pereval


# сериализатор пользователя - с миксином для уникальных полей, для устранения ошибки по емэйлу
class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']

    # переопределим save для соблюдения уникальности пользователя, т.к. с unique=True в модели не работал PATCH
    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),

            )
            return new_user


# сериализатор координат
class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


# сериализатор фотокарточек
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']


# сериализатор уровня сложности
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


# сериализатор перевалов (со вложенными сериализаторами)
class PerevalSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)
    level = LevelSerializer()

    class Meta:
        model = Pereval
        fields = ['id', 'status', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'coords', 'level', 'images']

    # переопределяем create для поддержки вложенных сериализаторов
    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user = User.objects.get_or_create(**user)[0]
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level)

        for image in images:
            data = image.pop('image')
            title = image.pop('title')
            Image.objects.create(data=data, title=title, pereval=pereval)

        return pereval

    # переопределяем update, т.к. при обновлении записи создавались новые сущности для координат и уровня сложности
    def update(self, instance, validated_data):
        # Обновление собственных полей сущности
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.add_time = validated_data.get('add_time', instance.add_time)
        instance.status = validated_data.get('status', instance.status)

        # Обновление связанных полей level
        level_data = validated_data.get('level', {})
        instance.level.summer = level_data.get('summer', instance.level.summer)
        instance.level.autumn = level_data.get('autumn', instance.level.autumn)
        instance.level.winter = level_data.get('winter', instance.level.winter)
        instance.level.spring = level_data.get('spring', instance.level.spring)
        instance.level.save()

        # Обновление связанных полей coords
        coords_data = validated_data.get('coords', {})
        instance.coords.latitude = coords_data.get('latitude', instance.coords.latitude)
        instance.coords.longitude = coords_data.get('longitude', instance.coords.longitude)
        instance.coords.height = coords_data.get('height', instance.coords.height)
        instance.coords.save()

        # Пользователя беру существующего
        user_data = validated_data.get('user', {})
        user = User.objects.get(**user_data)
        instance.user = user

        instance.save()
        return instance

    # Переопределяем валидацию для доп. проверки на неизменение данных пользователя
    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            user_data = data.get('user')
            validating_user_fields = [
                instance_user.email != user_data['email'],
                instance_user.phone != user_data['phone'],
                instance_user.fam != user_data['fam'],
                instance_user.name != user_data['name'],
                instance_user.otc != user_data['otc'],
            ]
            if user_data is not None and any(validating_user_fields):
                raise serializers.ValidationError('Данные пользователя не могут быть изменены')
        return data
