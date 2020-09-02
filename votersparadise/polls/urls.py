from django.urls import path
from django.conf.urls import url, include
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
  path(r"userprofile/follow",views.follow,name = "follow"),
  path(r"askquestion",views.askquestion,name="askquestion"),
  path(r"userprofile/unfollow",views.unfollow,name = "unfollow"),
  path(r"removeuser",views.removeuser,name="removeuser"),

  url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
  path(r"userprofile/<username>",views.userprofile,name="userprofile"),
  path(r"updateImage",views.updateImage,name="updateImage"),
  path(r"profile/delete_question",views.delete_question,name="delete_question"),
  path(r"profile/delete_account",views.delete_account,name="delete_account"),
]