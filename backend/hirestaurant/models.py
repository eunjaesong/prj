from django.db import models
from django.contrib.auth.models import AbstractUser # 회원 모델 
from .validators import * 

class User(AbstractUser): # AbstractUser 모델 상속 
    nickname = models.CharField(max_length=15,unique=True,null=True,
                                error_messages= {'unique':'이미 사용중인 닉네임'}
                                ) # 중복 닉네임 제한 
    
    profile_pic = models.ImageField(default="default_profile_pic.jpg",upload_to='profile_pics',
                                    blank=True
                                    ) # 유저 프로필사진 
    intro = models.CharField(max_length=60,blank=True)
    
    def __str__(self):
        return self.email
    # username은 무의하기 때문에 username대신 email을 보여준다
    # 왜냐하면 회원가입은 이메일로 하기 때문이다

# 식당정보 모델 

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    restaurant_link = models.URLField(validators=[validate_restaurant_list])
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    price_range = models.CharField(max_length=20)
    restaurant_image1 = models.ImageField(upload_to='restaurant_pics')
    restaurant_image2 = models.ImageField(upload_to='restaurant_pics',blank=True)
    restaurant_image3 = models.ImageField(upload_to='restaurant_pics',blank=True)
    
    def __str__(self):
        return self.restaurant_name