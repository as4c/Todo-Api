from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name='users'
urlpatterns = [
   path('signup/',csrf_exempt(views.SignupAPIView.as_view()),name='signup'),
   # path('signup/',views.Signup,name='signup'),
   path('login/',csrf_exempt(views.LoginAPIView.as_view()),name='login'),
   path('logout/',csrf_exempt(views.LogoutAPIView.as_view()),name='logout')
]