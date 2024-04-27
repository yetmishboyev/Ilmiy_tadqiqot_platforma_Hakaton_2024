from django.db import models
from django.contrib.auth.models import User
class Profil(models.Model):
    ism=models.CharField(max_length=50)
    fam=models.CharField(max_length=50)
    tel=models.CharField(max_length=13)
    rasm=models.FileField(upload_to='rasm_profil',null=True,blank=True)
    jins=models.CharField(max_length=5,null=True,blank=True)
    davlat=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    kasb=models.CharField(max_length=50,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.ism
class Maqola(models.Model):
    nom=models.CharField(max_length=100)
    Anotatsiya=models.TextField()
    kalit=models.TextField()
    adabiyot=models.TextField()
    fayl=models.FileField(upload_to='maqola')
    user_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom