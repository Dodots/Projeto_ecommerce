from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreateView, PerfilUpdateView, CreateSuccess, UpdateSuccess
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

app_name = "user"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('register/', UsuarioCreateView.as_view(), name="register"),
    path('update_data/', PerfilUpdateView.as_view(), name='update_data'),
    path('create_success', CreateSuccess.as_view(), name='create_user_success'),
    path('update_success', UpdateSuccess.as_view(), name='update_user_success'),
]
