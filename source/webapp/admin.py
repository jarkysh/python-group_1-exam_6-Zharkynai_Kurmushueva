from django.contrib import admin
from django.contrib.auth.models import User
from webapp.models import Post, UserInfo


class TopicInLine1(admin.StackedInline):
   model = User


class PostInLine2(admin.StackedInline):
   model = UserInfo

class AdminPost(admin.ModelAdmin):
   list_display = ["title","text","author",]





#admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Post, AdminPost)



#admin.site.register(User)
#admin.site.register(UserInfo)
#admin.site.register(Post)

