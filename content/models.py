from django.db import models


def image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    if instance.__class__ is Piece:
        return f"pieces/{instance.name}.{ext}"

    else:
        return f"artists/{instance.name}.{ext}"


# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=280)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Artist(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=280)
    image = models.ImageField(blank=True, null=True, default=None, upload_to=image_file_name)
    art = models.ForeignKey(Art, blank=True, null=True, default=None, on_delete=models.SET_NULL, related_name='artists')

    def __str__(self):
        return f"{self.id}: {self.name}"


class Piece(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=280)
    image = models.ImageField(blank=True, null=True, default=None, upload_to=image_file_name)
    artists = models.ManyToManyField(Artist, blank=True, default=None, related_name='exhibitions')
    public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
