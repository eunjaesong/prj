from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import (
    View,
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)

from hirestaurant.models import * 
from hirestaurant.forms import * 

# 접근제한자
from django.db.models import Q 
from django.contrib.contenttypes.models import ContentType
from typing import Any, Dict, List 




def index(request):
    print(request.user.is_authenticated)
    return render(request,'main/index.html') 


class RestaurantList(ListView):
    model = Restaurant
    template_name = "main/restraunt_list.html"
    context_object_name = "restraunt_list"
    paginate_by = 8

# 패스워드 변경 커스텀 페이지 만들기
class CustomPasswordChangeView(PasswordChangeView):
    # 오버라이딩 
    # 상속된 속성에 내용을 덧붙여서 다르게 사용 
    # 변경이 완료되면 리다이렉트 해주는 함수
    def get_success_url(self): 
        return reverse("index")
        