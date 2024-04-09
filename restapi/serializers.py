from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin, NestedUpdateMixin
from .models import User, Coords, Image, Level, Pereval


# сериализатор пользователя - с миксином для уникальных полей, для устранения ошибки по емэйлу
class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


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
