from django.db import models


# Своя модель пользователя
class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


# Модель координат перевала
class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


# модель для уровня сложности
class Level(models.Model):
    LEVEL_CHOICES = (
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б'),
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1А')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1А')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1А')
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1А')


# Модель перевала
class Pereval(models.Model):
    STATUS_CHOICES = (
        ("new", 'новый'),
        ("pending", 'на модерации'),
        ("accepted", 'модерация успешна'),
        ("rejected", 'информация не принята'),
    )

    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    level = models.OneToOneField(Level, on_delete=models.CASCADE)


# модель для хранения изображений
class Image(models.Model):
    title = models.CharField(max_length=255)
    data = models.ImageField()
    add_time = models.DateTimeField(auto_now_add=True)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
