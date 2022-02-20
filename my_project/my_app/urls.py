"""URl patterns for website"""

from django.urls import path
from . import views

app_name = "my_app"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("userinfo/", views.userinfo, name="userinfo"),
    path("thankingyou", views.thankingyou, name="thankingyou"),
    path("form/", views.users, name="users"),

]
