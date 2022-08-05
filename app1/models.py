from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    ism=models.CharField(max_length=120)
    username=models.CharField(max_length=120)
    rasm=models.URLField(blank=True)
    bio=models.CharField(max_length=500,blank=True)
    public=models.BooleanField(default=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Connection(models.Model):
    follower=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="follower")
    following=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="following")

class Post(models.Model):
    matn=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    joy=models.CharField(max_length=120)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return self.profil
class Media(models.Model):
    fayl=models.URLField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

class Like(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        unique_together=[["profil","post_id"]]

class Comment(models.Model):
    matn=models.CharField(max_length=500)
    sana=models.DateField(auto_now_add=True)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)

class Comment_like(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    class Meta:
        unique_together=[["comment","profil"]]

class Xabar(models.Model):
    matn = models.CharField(max_length=500)
    vaqt = models.DateTimeField(auto_now_add=True)
    jonatuvchi=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="xabar_jonatuvchi")
    qabul=models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="xabar_qabulqiluvchi")

class Reaksiya_xabar(models.Model):
    reaksiya = models.CharField(max_length=500)
    xabar=models.ForeignKey(Xabar,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)