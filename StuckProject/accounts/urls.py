from django.urls import path, register_converter
from accounts import views
from .converters import NegativeIntConverter
register_converter(NegativeIntConverter, 'negint')

app_name = 'accounts'

urlpatterns = [
    # 로그인
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # 마이페이지
    path('mypage/', views.mypage, name="my-page"),

    # 아이디 찾기
    path('forgot_id/', views.forgot_id, name="forgot_id"),

    # 마이페이지
    path('mypage/<int:year>/<int:month>/<int:day>/<negint:week_offset>/', views.mypage, name='mypage_by_date'),
]