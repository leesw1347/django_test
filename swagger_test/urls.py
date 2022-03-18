from django.urls import path
# from swagger_test.views import UserList , user_detail , user_detail2, user_detail3
from rest_framework import status

from swagger_test.views import *

"""
클래스 기반 뷰 기능 (as_view)를 아래와 같이 사용할 수도 있다
"""


class LoginResponseSerializer(Serializer):
    pass


decorated_login_view = swagger_auto_schema(
    method="post" ,
    responses={
        status.HTTP_200_OK: LoginResponseSerializer
    }
)  # (LoginView.as_view())

urlpatterns = [
    path("v1/test" , UserList.as_view() , name="UserList") ,
    path("v1/user_detail/" , user_detail , name="user_detail") ,
    path("v1/user_detail2/" , user_detail2 , name="user_detail2") ,
    path("v1/user_detail3/" , user_detail3 , name="user_detail3") ,
    path("v1/articles/today/" , ArticleViewSet.as_view , name="articles.today") ,
]
