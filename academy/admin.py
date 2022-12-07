from django.contrib import admin
from .models import sport_detail,Membership_plan,Coach_Detail,Member_Feedback,Event,Member_Detail


class Admin_Coach(admin.ModelAdmin):
    list_display=('Name','Email','phone','Experience')
    search_fields=('Name',)


class Admin_sport(admin.ModelAdmin):
    list_display=('Sport_name','Sport_type','Description')
    search_fields=('Sport_type',)#it used for searching


class Admin_Member(admin.ModelAdmin):
    list_display=('name','phone','city','plan_name')
    search_fields=('city',)
    list_filter=['plan_name','city','age']

admin.site.register(sport_detail,Admin_sport)
admin.site.register(Membership_plan)
admin.site.register(Coach_Detail,Admin_Coach)#it will show data in tabular formate
admin.site.register(Member_Feedback)
admin.site.register(Event)
admin.site.register(Member_Detail,Admin_Member)



admin.site.site_header="Sports Academy Administration"
admin.site.site_title="Sports Admin Dashboard"
admin.site.index_title="Welcome to Our Portal"



# Register your models here.
