from django.db import models


# Своя модель пользователя
class User(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


# Модель координат перевала
class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


# Модель перевала
class Pereval(models.Model):
    STATUS_CHOICES = (
        ("new", 'новый'),
        ("pending", 'на модерации'),
        ("accepted", 'модерация успешна'),
        ("rejected", 'информация не принята'),
    )
    LEVEL_CHOICES = (
        ('1A', '1А'),
        ('1B', '1Б'),
        ('2A', '2А'),
        ('2B', '2Б'),
        ('3A', '3А'),
        ('3B', '3Б'),
    )
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    level_winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    level_spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    level_summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    level_autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')


# модель для хранения изображений
class Image(models.Model):
    title = models.CharField(max_length=255)
    data = models.ImageField()
    add_time = models.DateTimeField(auto_now_add=True)


# промежуточная таблица для связи таблиц перевалов и изображений
class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
