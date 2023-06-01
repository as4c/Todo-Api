from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes


class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email=     request.data.get('email')
        if not username or not password:
            return Response({'error': 'username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'email already exists'}, status=400)
        

        user = User(username=username)
        user.set_password(password)
        user.save()

        return Response({'message': 'User created successfully'}, status=201)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def Signup(request,*args,**kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    email=     request.data.get('email')
    if not username or not password:
        return Response({'error': 'username and password are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'email already exists'}, status=400)
    

    user = User(username=username)
    user.set_password(password)
    user.save()

    return Response({'message': 'User created successfully'}, status=201)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]


    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=200)
        else:
            return Response({'error': 'Invalid username or password'}, status=401)


class LogoutAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=200)
