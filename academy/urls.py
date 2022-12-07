from django.urls import path,include
from.import views#used . for current directory
urlpatterns = [
  path("",views.home,name="home"),  
  path("contactus/",views.contactus,name="contactus"),
  path("aboutus/",views.aboutus,name="about"),
  path("feedback/",views.feedback,name="feedback"),
  path('sportsdetails/',views.sports,name="sports_details"),
  path('coachdetails/',views.coachdetails,name="coachdetails"),
  path('plandetails/',views.plandetails,name="plandetails"),
  path('member_registration/',views.member_registration,name="registration"),
  path('member_login/',views.member_login,name="member_login"),
  path('member_edit_profile/',views.member_edit_profile,name="member_edit_profile"),
  path('member_logout/',views.member_logout,name="member_logout"),
  path('member_view_profile/',views.member_view_profile,name="member_view_profile"),
  path('library/',views.library,name="library"),
  path('gym/',views.gym,name="gym"),
  path('cafeteria/',views.cafeteria,name="cafeteria"),
  path('kabaddi/',views.kabaddi,name="kabaddi")
]