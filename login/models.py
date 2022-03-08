from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=60,verbose_name="Email")
    password=models.CharField(max_length=15,verbose_name="Password")
    avatar=models.ImageField(upload_to='login/imagenes/', default='imagenes/profile_default.png',verbose_name="Avatar")
    
    def __str__(self):
        return self.email + "--" + self.password
    
    def delete(self, using=None,keep_parents=False):
        self.avatar.storage.delete(self.avatar.name)
        super().delete()
    