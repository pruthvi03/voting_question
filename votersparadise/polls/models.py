from django.db import models
from django.contrib.auth.models import User


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'following')
    following_user_id = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = 'followers')
    created = models.DateTimeField(auto_now_add=True)

class QuestionTable(models.Model):
    question_text = models.CharField(max_length = 300 ,null = False )
    pub_date = models.DateTimeField(auto_now_add=True)
    group_code = models.CharField(max_length = 20)
    op1 = models.CharField(max_length = 100)
    op2 = models.CharField(max_length = 100)
    op3 = models.CharField(max_length = 100 ,null = True)
    op4 = models.CharField(max_length = 100 ,null = True)

