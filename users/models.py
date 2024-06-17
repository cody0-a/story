from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from django.urls  import reverse
from PIL import Image

from io import BytesIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_pics',blank=True)
    fullname = models.CharField(max_length=256,blank=True)

    bio = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.user.first_name
    
    def get_absolute_url(self):
        return reverse("users:profile",kargs=[str(self.user.id)])
    
    def photo_url(self):
        if self.img:
            return self.img.url
        else:
            return "/media/profile_pics/default.png"
        

    def resize_image(instance, filename, size=(800, 600)):
 

        img = Image.open(instance.image)
        img.thumbnail(size, resample=Image.BICUBIC)

        thumb_io = BytesIO()
        img.save(thumb_io, filename.split('.')[-1].upper())

        resized_image = ContentFile(thumb_io.getvalue())
        return resized_image



