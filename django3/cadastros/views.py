from tokenize import group
import django
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Atividades, Campo, Conquistas, Ideias, MeusProjetos, Relatorios
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class CampoCreate(LoginRequiredMixin, CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class MeusProjetosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = MeusProjetos
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-meusprojetos')
    login_url = reverse_lazy("login")   
    
    def form_valid(self, form):
        form.instance.campo = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class RelatoriosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Relatorios
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.campo = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class IdeiasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Ideias
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.campo = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context


class AtividadesCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Atividades
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena']
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.campo = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context


class ConquistasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Conquistas
    group_required = [u'adm-clio',
                      u'adm-aries', u'adm-hera', u'adm-athena']
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-conquistas')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.campo = self.request.user
        url = super().form_valid(form)
        return url
           
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

    # UPDATE


class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def get_object(self, queryset = None):
        self.object = get_object_or_404(Campo, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de campus"
        context['botao'] = "Salvar"
        return context

class MeusProjetosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = MeusProjetos
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-meusprojetos')
    def get_object(self, queryset = None):
        self.object = get_object_or_404(MeusProjetos, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class RelatoriosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Relatorios
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Relatorios, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class IdeiasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Ideias
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Ideias, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class AtividadesUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Atividades
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio',
                      u'adm-aries', u'adm-hera', u'adm-athena']
    success_url = reverse_lazy('listar-atividades')
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Atividades, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class ConquistasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Conquistas
    fields = ['assunto', 'arquivo', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    group_required = [u'adm-clio',
                      u'adm-aries', u'adm-hera', u'adm-athena']
    success_url = reverse_lazy('listar-conquistas')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Conquistas, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

# DELETE


class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Campo
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Campo, pk=self.kwargs['pk'], campo=self.request.user)
        return self.object


class MeusProjetosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = MeusProjetos
    template_name = 'cadastros/formulario-excluir.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-meusprojetos')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(MeusProjetos, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class RelatoriosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Relatorios
    template_name = 'cadastros/formulario-excluir.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Relatorios, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class IdeiasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Ideias
    template_name = 'cadastros/formulario-excluir.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Ideias, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class AtividadesDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Atividades
    template_name = 'cadastros/formulario-excluir.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena']
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Atividades, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object 

class ConquistasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Conquistas
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-conquistas')
    group_required = [u'adm-clio',
                      u'adm-aries', u'adm-hera', u'adm-athena']
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(
            Conquistas, pk=self.kwargs['pk'], campo=self.request.user)
        return self.object

# LISTAR 


class CampoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Campo
    lista = 'cadastros/campo.html'
    login_url = reverse_lazy("login")

    def get_queryset(self):
        self.object_list = Campo.objects.filter(nome = self.request.user)
        return super().get_queryset()


class MeusProjetosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = MeusProjetos
    template_name = 'cadastros/meusprojetos.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    login_url = reverse_lazy("login")
    paginate_by = 10

    def get_queryset(self):
        self.object_list = MeusProjetos.objects.filter(campo=self.request.user)
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = MeusProjetos.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = MeusProjetos.objects.all()
        return pesquisa and self.object_list

class RelatoriosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Relatorios
    template_name = 'cadastros/relatorios.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        self.object_list = Relatorios.objects.filter(campo=self.request.user)
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Relatorios.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Relatorios.objects.all()
        return pesquisa and self.object_list

class IdeiasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Ideias
    template_name = 'cadastros/ideias.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        self.object_list = Ideias.objects.filter(campo=self.request.user)
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Ideias.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Ideias.objects.all()
        return pesquisa and self.object_list

class AtividadesList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Atividades
    template_name = 'cadastros/atividades.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera',
                      u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    login_url = reverse_lazy("login")
    paginate_by = 10

    def get_queryset(self):
        self.object_list = MeusProjetos.objects.filter(campo=self.request.user)
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Atividades.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Atividades.objects.all()
        return pesquisa

class ConquistasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Conquistas
    template_name = 'cadastros/conquistas.html'
    group_required = [u'adm-clio', u'adm-aries', u'adm-hera', u'adm-athena', u"clio", u"aries", u"hera", u"athena"]
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Conquistas.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Conquistas.objects.all()
        return pesquisa