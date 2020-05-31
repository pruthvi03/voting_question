from django.urls import path
from . import views

urlpatterns = [
 path("",views.index,name = "home"),
 path(r"signup",views.signup,name = "signup"),
 path(r"passwordreset",views.passreset,name= "handlePasswordReset"),
  path(r"login",views.handlelogin,name = "handlelogin"),
 path(r"logout",views.handlelogout,name = "handlelogout"),
 path(r"profile",views.profile,name = "profile"),
 path(r"search",views.search,name = "search"),
 path(r"following",views.following,name = "following"),
 path(r"followers",views.followers,name = "followers"),
  path(r"follow",views.follow,name = "follow"),


]