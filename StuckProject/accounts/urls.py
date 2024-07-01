from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # 로그인
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # 마이페이지
    path('mypage/', views.mypage, name="my-page")
]