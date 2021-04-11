from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil


class UsuarioCreateView(CreateView):
    template_name = "user/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('user:create_user_success')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="membro")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


class PerfilUpdateView(UpdateView):
    template_name = "user/form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("user:update_user_success")

    def get_object(self):
        self.get_object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.get_object


class CreateSuccess(TemplateView):
    template_name = "user/create_user_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_conta'] = 'Sua conta foi criada com sucesso!'
        return context

class UpdateSuccess(TemplateView):
    template_name = "user/create_user_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_conta'] = 'Sua conta foi atualizada com sucesso!'
        return context