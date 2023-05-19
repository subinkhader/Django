from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from store.models import Medicinedetails
from rest_framework.status import(
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    HTTP_204_NO_CONTENT,
    HTTP_205_RESET_CONTENT,
    HTTP_206_PARTIAL_CONTENT,
    HTTP_207_MULTI_STATUS,
    HTTP_208_ALREADY_REPORTED,
    HTTP_226_IM_USED,
)


from .serializers import MedicineSerializer, SignupSerializer

# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registration(request):
    obj = SignupSerializer(data=request.data)
    if obj.is_valid():
        obj.save()
        return Response({'message':'Successfully registered'},status=HTTP_200_OK)
    return Response(obj.errors,status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password') 
    
    if username is None or password is None:
        return Response({'message': 'Enter a valid username and password'},status=HTTP_400_BAD_REQUEST)
    user = authenticate(username = username, password = password)
    
    if not user:
         return Response({'message': 'Invalid credential'},status=HTTP_400_BAD_REQUEST)
    token,_ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},status=HTTP_200_OK)


@csrf_exempt        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response('User Logged out successfully')


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated))
def addmedicine(request):
    serializer = MedicineSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated))
def listmedicine(request):
    med = Medicinedetails.object.all()
    medi = MedicineSerializer(med, many=True)
    return Response(medi.data)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated))
def viewmedicine(request,id):
    med = Medicinedetails.objects.get(pk=id)
    medi = MedicineSerializer(med)
    return Response(medi.data)
    
@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated))
def delete(request):
    med = Medicinedetails.objects.get(pk=id)
    med.delete()
    return Response(status=HTTP_200_OK)

@csrf_exempt
@api_view(["PUT"])
@permission_classes((IsAuthenticated))
def update(request):
    med = Medicinedetails.objects.get(pk=id)
    upd = MedicineSerializer(med,data=request.data)
    if upd.is_valid():
        upd.save()
        return Response(upd.data)