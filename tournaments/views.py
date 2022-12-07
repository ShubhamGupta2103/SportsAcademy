from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from django.views import View
from.models import Enrollment, Tournament
from django.contrib import messages

def t_home(request):
    # return HttpResponse("<h1>This is a tournaments home page </h1>")
    return render(request,'tournaments/html/tournaments_home.html')

def t_about(request):
    return HttpResponse("<h1>This is a tournaments about  page </h1>")


class TournamentDetail(View):#class based view used to simply the code and use for customer
    def get(self,request):
        t_queryset=Tournament.objects.all()
        t_dict={
            "t_data":t_queryset
        }
        return render(request,'tournaments/html/tournament_detail.html',t_dict)

def sponsers(request):
    return render(request,'tournaments/html/sponsers.html')


def enroll(request):
    if request.method=="GET":
        enroll_objects=Enrollment.objects.all()
        enroll_dict={"enroll_key":enroll_objects}
        return render(request,'tournaments/html/enrollment.html',enroll_dict)

    if request.method=="POST":
        
        enroll_name=request.POST["txtname"]
        enroll_age=request.POST["txtage"]
        enroll_email=request.POST["txtemail"]
        enroll_phone=request.POST["txtphone"]
        enroll_tournament_name=request.POST["cmbname"]
        
        enroll_city=request.POST["cmbcity"]
        enroll_address=request.POST["txtaddress"]

        enroll_gender=request.POST["gender"]
        
        if int(enroll_age)<18 or int(enroll_age)>60:
             messages.success(request,"You are not eligible for enrollment")
             return render(request,'tournaments/html/enrollment.html')

        elif len(enroll_phone)>10 or int(enroll_phone)<10 or int(enroll_phone)<0:
             messages.success(request,"Please enter a valid phone number for enrollment")
             return render(request,'tournaments/html/enrollment.html')


        else:
            new_member=Tournament(name=enroll_name,age=enroll_age,email=enroll_email,phone=enroll_phone,city=enroll_city,address=enroll_address,tournament_name=enroll_tournament_name,Gender=enroll_gender)
            new_member.save()
            print("enrollment successfully")
            messages.error(request,"Thank you for being enroll")
            return render(request,'tournaments/html/enrollment.html')






