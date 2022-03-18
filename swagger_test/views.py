from django.http import HttpResponse

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view , action
from rest_framework.parsers import MultiPartParser
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

"""
class-based view를 표현하기 위해선 아래와 같이 설정할 수 있다.
"""


class UserSerializer(Serializer):
    pass


class UserList(APIView):
    @swagger_auto_schema(
        responses={
            200: UserSerializer(many=True)
        }
    )
    def get(self , request):
        print(request)

    @swagger_auto_schema(operation_description='UserList의 post 메소드 결과값을 반환한다')
    def post(self , request):
        print(request)


"""
ViewSet, GenericViewSet의 경우, ModelViewSet이 여러경로에 대응하는 경우, 액션메소드를 반영해서 작업할 수 있다.
"""


# 직접 구현하지 않은, 메소드의 생성을 사용자 지정하려면 method_decorator를 함께 사용할 수 있다
# 이렇게 구현하면, 메소드를 불필요하게 재정의하는 것을 방지할 수 있다
# @method_decorator(decorator=swagger_auto_schema(
#     operation_description="description from swagger_auto_schema_via method_decorator"
# ) , name="today")
class ArticleViewSet(viewsets.ModelViewSet):

    @swagger_auto_schema(
        method="get" ,
        operation_description="GET 메소드"
    )
    @api_view(http_method_names=["get"])
    def get(self , request):
        return HttpResponse()

    @swagger_auto_schema(
        method="post" ,
        operation_description="POST 메소드"
    )
    @action(methods=["post"], detail=False)
    def post(self , request):
        return HttpResponse()

    # auto_swagger_schema 데코레이터에서 method를 지정해주지 않으면 디폴트로 GET만 처리할 수 있도록 한다
    @swagger_auto_schema(operation_description="GET /articles/today/")
    @action(methods=["get"] , detail=False)
    def today(self , request):
        print(request)

    @swagger_auto_schema(
        method="get" ,
        operation_description="GET /articles/{id}/image/")
    @swagger_auto_schema(
        method="post" ,
        operation_description="POST /articles/{id}/image/")
    @action(methods=["get" , "post"] , detail=True , parser_classes=(MultiPartParser ,))
    def image(self , request , id=None):
        print(request)

    @swagger_auto_schema(operation_description="PUT /articles/{id}/")
    def update(self , request , *args , **kwargs):
        print(request)

    @swagger_auto_schema(operation_description="PATCH /articles/{id}/")
    def partial_update(self , request , *args , **kwargs):
        print(request)


"""
GET Method만 swagger에서 보여지도록 설정할 수 있다
"""


@swagger_auto_schema(
    methods=["PUT"] ,
    auto_schema=None
)
@swagger_auto_schema(
    methods=["GET"]
)
@api_view(["GET" , "PUT"])
def user_detail(request):
    print(request)
    return HttpResponse()


"""
뷰 함수에서 데코레이터를 사용하여 생성된 일부 속성을 재정의 할 수 있다
"""


@swagger_auto_schema(operation_description="유저디테일정보" , responses={
    404: "user_not_found"
})
def user_detail2(request , *args , **kwargs):
    print("user_detail2 " , request)
    return HttpResponse()


"""
함수기반 @apiview의 경우에는 동일한 보기가 여러메소드를 처리할 수 있으므로, 데코레이터가 중복으로 나타난다
"""
test_param = openapi.Parameter(name="test" , in_=openapi.IN_QUERY , description="test manual param1" ,
                               type=openapi.TYPE_BOOLEAN)
test_param2 = openapi.Parameter(name="응답값" , in_=openapi.IN_QUERY , description="응답값 호출에 활용하는 객체" ,
                                type=openapi.TYPE_INTEGER)
user_response = openapi.Response(description="응답값 객체" , schema=UserSerializer)


@swagger_auto_schema(
    method="GET" ,
    manual_parameters=[test_param , test_param2] ,
    responses={
        200: user_response
    }
)
@swagger_auto_schema(methods=["PUT" , "POST"] , request_body=UserSerializer)  # 또는 methods 파라미터를 통해서 List로 method를 받아들이게 할수도 있다
@api_view(["GET" , "POST" , "PUT"])
def user_detail3(request):
    print(request)
    return HttpResponse()
