from django.db import models
from django.contrib.auth.models import User


class UserFollowing(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE, default="")
    following = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'following', blank=True, null=True)
    profile_pic = models.ImageField(upload_to = "polls/profile_pic" , default = "")
    followers = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'followers', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "following")
        unique_together = ("user","followers")

    def __str__(self):
       return self.user.username

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

