from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class UserList(APIView):
    swagger_schema = None # swagger 생성을 제거하기 위해선 이렇게 설정할 수 있음

# GET Method만 swagger에서 보여지도록 설정할 수 있다
@swagger_auto_schema(
    methods=["PUT"],
    auto_schema=None
)
@swagger_auto_schema(
    methods=["GET"]
)
@api_view(["GET", "PUT"])
def user_detail(request):
    print(request)
    return HttpResponse()

# 뷰 함수에서 데코레이터를 사용하여 생성된 일부 속성을 재정의 할 수 있다
@swagger_auto_schema(operation_description="유저디테일정보", responses={
    404: "user_not_found"
})
def user_detail2(request, *args, **kwargs):
    print("user_detail2 ", request)
    return HttpResponse()

"""
"""