from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='Default.jpg',upload_to='Profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        try:
            old_instance = Profile.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Profile.DoesNotExist:
            pass

        super().save(*args,**kwargs)

        img = Image.open(self.image.path)
        img = img.convert('RGB')
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# edit save funtion to delete previous image before saving new.