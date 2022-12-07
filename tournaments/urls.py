from .import views
from django.urls import path,include
urlpatterns=[
    path('',views.t_home,name="t_home"),
    path('about/',views.t_about,name="t_about"),
    path('details/',views.TournamentDetail.as_view(),name="detail"),
    path('sponsers/',views.sponsers,name="sponsers"),
    path('enroll/',views.enroll,name="enroll"),

]