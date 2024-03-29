from operator import truediv
from django.db import models

from django.utils import timezone

class sport_detail(models.Model):
    Sport_name=models.CharField(max_length=45,primary_key=True)
    Sport_type=models.CharField(max_length=30,null=False,default="Indoor")
    Description=models.TextField()
    Date=models.DateField(default=timezone.now)


class Membership_plan(models.Model):
    plane_name=models.CharField(max_length=50,primary_key=True)
    Duration=models.CharField(max_length=45,null=False)
    charge=models.IntegerField(null=False,default=0)
    Description=models.TextField()


    def __str__(self):
        return self.plane_name+self.Duration

Gender=[
    ("M","Male"),
    ("F","Female")
]

class Coach_Detail(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=10,null=False)
    Gender=models.CharField(max_length=6,choices=Gender,null=False)
    Experience=models.CharField(max_length=20,null=False)
    About_coach=models.TextField()

class Contact(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=10,null=False)
    your_query=models.TextField()
    Date=models.DateField(default=timezone.now)

class Member_Feedback(models.Model):
    Name=models.CharField(max_length=50,default="",null=False)
    rating=models.IntegerField(default=1)
    feedback_text=models.TextField()
    Date=models.DateField(default=timezone.now)

class Event(models.Model):
    event_name=models.CharField(max_length=50,null=False)
    event_description=models.TextField()
    event_venue=models.CharField(max_length=180)
    event_pic=models.FileField(max_length=100,upload_to="academy/picture",default="")
    event_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.event_name
        


class Member_Detail(models.Model):
    member_id=models.CharField(primary_key=True,max_length=45)
    password=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=45)
    address=models.TextField()
    gender=models.CharField(max_length=6)
    plan_name=models.CharField(max_length=50)
    transaction_no=models.CharField(max_length=100,null=False)
    date=models.DateField(default=timezone.now)




