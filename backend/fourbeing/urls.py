from django.urls import path
from . import views
from knox import views as knox_views
from fourbeing.views import LoginView, CreateUserView, ManageUserView


urlpatterns = [
    path('api/auth/createuser/', CreateUserView.as_view(), name="createuser"),
    path('api/auth/profile/', ManageUserView.as_view(), name='profile'),
    path('api/auth/login/', LoginView.as_view(), name='knox_login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/test/', views.test, name='test'),

]