from email import message
from django.shortcuts import render,HttpResponse,redirect
from .models import sport_detail,Contact,Coach_Detail,Membership_plan,Member_Feedback,Event,Member_Detail
from django.contrib import messages
def home(request):
    event_objects=Event.objects.all()
    event_dict={
        "event_key":event_objects
    }
    return render(request,'academy/html/index.html',event_dict)

def contactus(request):
    return (HttpResponse("<h2>This is a contactus </h2>"))

def aboutus(request):
    return render(request,'academy/html/abouts.html')

def feedback(request):
    if request.method=="GET":
        return render(request,'academy/html/feedback.html')
    if request.method=="POST": #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtname"]
        user_rate=request.POST["txtrate"]
        user_feedback=request.POST["txtfeedback"]
        m=Member_Feedback(Name=user_name,rating=user_rate,feedback_text=user_feedback)# object creation
        m.save()# object saving and it will store data into Contact table using ORM
        print("feedback saved successfully")
        return render(request,'academy/html/feedback.html')

    
def about(request):
    return(HttpResponse("<h2>This is a aboutus page </h2>"))

def feed(request):
    return(HttpResponse("<h1 style='color:green'>This is a feedback page</h1>"))

def contactus(request):
    if request.method=="GET":
        return render(request,'academy/html/contactus.html')
    if request.method=="POST": #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtname"]
        user_email=request.POST["txtemail"]
        user_phone=request.POST["txtphone"]
        user_query=request.POST["txtquery"]
        c=Contact(Name=user_name,Email=user_email,phone=user_phone,your_query=user_query)# object creation
        c.save()# object saving and it will store data into Contact table using ORM
        print("Contact saved successfully")
        messages.success(request,"Thank you for contacting us ")
        return render(request,'academy/html/contactus.html')

def coachdetails(request):
        return render(request,'academy/html/coachdetails.html')

def library(request):
        return render(request,'academy/html/library.html')


def gym(request):
        return render(request,'academy/html/gym.html')

def cafeteria(request):
        return render(request,'academy/html/cafeteria.html')

def kabaddi(request):
        return render(request,'academy/html/kabaddi.html')





                   


    
# to show the details  of all sports
def sports(request):
    sports_objects=sport_detail.objects.all()#it returns queryset
    print(type(sports_objects))

#How to send data on an html template from view
    sports_dict={
        "sport_data":sports_objects
    }

    return render(request,'academy/html/allsports.html',sports_dict)

def coachdetails(request):
    coach_objects=Coach_Detail.objects.all()#it returns queryset
    
#How to send data on an html template from view
    coach_dict={
        "coach_data":coach_objects
    }

    return render(request,'academy/html/coachdetails.html',coach_dict)


def plandetails(request):
    plan_objects=Membership_plan.objects.all()#it returns queryset
    
#How to send data on an html template from view


    plan_dict={
        "plan_data":plan_objects
    }
    return render(request,'academy/html/plandetails.html',plan_dict)

def member_registration(request):
    if request.method=="GET":
        plan_objects=Membership_plan.objects.all()
        plan_dict={"plan_key":plan_objects}
        return render(request,'academy/html/registration.html',plan_dict)

    if request.method=="POST":
        member_id=request.POST["txtuserid"]
        member_pass=request.POST["txtuserpass"]
        member_name=request.POST["txtname"]
        member_phone=request.POST["txtphone"]
        member_address=request.POST["txtaddress"]
        member_city=request.POST["cmbcity"]
        member_gender=request.POST["gender"]
        member_age=request.POST["txtage"]
        member_transaction=request.POST["txttransaction"]
        member_plan_name=request.POST["cmb_plan"]
        # len(member_age)>2 or int(member_age)<0:
        if int(member_age)<18 or int(member_age)>60:
             messages.success(request,"You are not eligible")
             return render(request,'academy/html/registration.html')

        elif len(member_phone)>10 or int(member_phone)<10 or int(member_phone)<0:
             messages.success(request,"Please enter a valid phone number")
             return render(request,'academy/html/registration.html')


        else:
            new_member=Member_Detail(member_id=member_id,password=member_pass,name=member_name,age=member_age,phone=member_phone,city=member_city,address=member_address,gender=member_gender,plan_name=member_plan_name,transaction_no=member_transaction)
            new_member.save()
            print("Member registered successfully")
            messages.error(request,"Thank you for being a Member")
            return render(request,'academy/html/registration.html')

def member_login(request):
    if request.method=="GET":
      return render(request,'academy/html/login.html')

    if request.method=="POST":
        mem_id=request.POST["userid"]
        mem_password=request.POST["userpass"]

        member_query_set=Member_Detail.objects.filter(member_id=mem_id,password=mem_password)
        print(len(member_query_set))
        if len(member_query_set)>0:
            request.session["member_session"]=mem_id#builtin dictionary 
            
            member_object={"member_data":member_query_set}
            return render(request,'academy/html/member/member_home.html',member_object)
            

        else:
            messages.error(request,"Invalid Credential")
            return render(request,'academy/html/login.html')

def member_edit_profile(request):
    if "member_session" not in request.session.keys():
        return redirect("member_login")

    if request.method=="GET":
        loggedIn_member_Id=request.session["member_session"]
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_Id)
        member_dict={
            "member_data":member_object
        }

        return render(request,'academy/html/member/member_editprofile.html',member_dict)

    if request.method=='POST':
        ph=request.POST["phone"]
        add=request.POST["address"]
        loggedIn_member_Id=request.session["member_session"]
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_Id)
        
        member_object.phone=ph
        member_object.address=add
        member_object.save()
        member_dict={
            "member_data":member_object
        }

        messages.success(request,"Profile updated successfully")

        return render(request,'academy/html/member/member_editprofile.html',member_dict)


def member_logout(request):
    if "member_session" not in request.session.keys():
        return redirect("member_login")


    del request.session["member_session"]#it is used to destroy the session
    return redirect("member_login")

##view profile##
def member_view_profile(request):

    if "member_session" not in request.session.keys():
        return redirect("member_login")
        
    if request.method=="GET":
        loggedIn_member_Id=request.session["member_session"]#fetch
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_Id)

        member_dict={
            "member_data":member_object
        }

        return render(request,'academy/html/member/member_view_profile.html',member_dict)
        




         
        



