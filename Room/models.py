from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#created new table in db 
class pay(models.Model):
    bookid=models.IntegerField()
class bookings(models.Model):
    bookingid=models.IntegerField()
class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    gen=models.CharField(max_length=30,null=True)
    add=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)
    birth=models.DateField(null=True)
    proof=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.username

class State(models.Model):
    state=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    ownername=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.state,self.username,self.ownername,self.date


class District(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    dist=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.dist+" "+self.state.state


class Status(models.Model):
    status = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status


class Owner_Detail(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    register=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    dist=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    local_add = models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=100,null=True)
    rent=models.IntegerField(null=True)
    img=models.FileField(null=True)

    def __str__(self):
        return self.register.user.username


class Image(models.Model):
    owner=models.ForeignKey(Owner_Detail,on_delete=models.CASCADE,null=True)
    room_name=models.CharField(max_length=100,null=True)
    img=models.FileField(null=True)
    def __str__(self):
        return self.owner.register.user.username+" "+self.room_name





