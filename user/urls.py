from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreateView, PerfilUpdateView
from django.urls import reverse_lazy

app_name = "user"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('register/', UsuarioCreateView.as_view(), name="register"),
    path('update_data/', PerfilUpdateView.as_view(), name='update_data')
]