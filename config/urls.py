from django.contrib import admin
from django.urls import path, include

from blog import views
from member import views as member_views

urlpatterns = [
    path("admin/", admin.site.urls),

    #blog
    path('', views.blog_list, name="blog_list"),
    path('<int:pk>/', views.blog_detail, name="blog_detail"),

    # Authentication 코드 추가
    # Django에 내장된 url 사용
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', member_views.sign_up, name='signup'),
    path('login/', member_views.login, name='login'),
]
