from django.db import models
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return "register/static/images/%s.%s" % (instance.user.id, ext)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, default=None, upload_to=content_file_name)

    REQUIRED_FIELDS = ['user']

    def __str__(self):
        return self.user.__str__()

