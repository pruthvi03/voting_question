from django.contrib import admin
from .models import UserFollowing,QuestionTable,UserInfo,Given_ans
# Register your models here.

admin.site.register(UserFollowing)
admin.site.register(QuestionTable)
admin.site.register(UserInfo)
admin.site.register(Given_ans)
