from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tag, Restaurant, User, Review



admin.site.register(User,UserAdmin) # 유저 모델의 정보를 모두 보여주길
UserAdmin.fieldsets += (('Custom fields',{'fields':('nickname','profile_pic',)}),)# custom fields라는 섹션 아래에 nickname fields라는 필드를 새로 추가해줌

admin.site.register(Restaurant)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(Tag, TagAdmin)