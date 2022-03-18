from django.urls import path

from swagger_test.views import UserList , user_detail , user_detail2

urlpatterns = [
    path("v1/test" , UserList.as_view() , name="UserList") ,
    path("v1/user_detail/" , user_detail , name="user_detail") ,
    path("v1/user_detail2/" , user_detail2 , name="user_detail2")
]
