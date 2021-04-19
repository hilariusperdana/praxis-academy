from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    my_photo = models.ImageField(default='pp.png', upload_to='dp/')
    first_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=False, null=False, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=14)

    joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)