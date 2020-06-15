from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    profile_pic = models.ImageField(default = "profilepic.png",blank=True,null=True)
    name = models.OneToOneField(User,on_delete = models.CASCADE,related_name="name")
    
    def __str__(self):
       return self.name.username

class UserFollowing(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'user', blank=True, null=True)
    following = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'following', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.following.username 

class Groupcode(models.Model):
    groupcode = models.CharField(max_length = 15)    

class QuestionTable(models.Model):

    question_text = models.CharField(max_length = 300 ,null = False )
    pub_date = models.DateTimeField(auto_now_add=True)
    group_code = models.ForeignKey(Groupcode , on_delete = models.CASCADE)
    op1 = models.CharField(max_length = 100)
    op2 = models.CharField(max_length = 100)
    op3 = models.CharField(max_length = 100 ,null = True)
    op4 = models.CharField(max_length = 100 ,null = True)
    auther = models.ForeignKey(User,on_delete = models.CASCADE)

