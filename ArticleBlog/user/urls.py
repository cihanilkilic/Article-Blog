from django.urls import path
from .import views

app_name="user"
urlpatterns = [
    path('register/',views.User_Register,name="User_Register"),
    path('login/',views.User_Login,name="Login"),
    path('logout/',views.logoutView,name="Logout"),

]
