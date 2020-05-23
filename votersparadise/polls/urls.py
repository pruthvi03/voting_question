from django.urls import path
from . import views

urlpatterns = [
 path("",views.index,name = "home"),
 path(r"signup",views.signup,name = "signup"),
 path(r"passwordreset",views.passreset,name= "handlePasswordReset"),
  path(r"login",views.handlelogin,name = "handlelogin"),
 path(r"logout",views.handlelogout,name = "handlelogout"),

]