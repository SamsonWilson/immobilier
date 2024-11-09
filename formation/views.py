from msilib.schema import ListView
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Ville,Client
from .form import VilleForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Client, Ville


class IndexView(TemplateView):
    template_name = 'index.html'

class FormView(CreateView):
    model = Ville
    fields = ["nomV","nomQ","numM", "descriptionV", "imageQ","imageM","imageCH","user"]  
    template_name = 'Flogement.html'
    success_url = reverse_lazy('villes_list') 
    login_url = 'account_login'

    def form_valid(self, form):
        latitude = self.request.POST.get('latitude')
        longitude = self.request.POST.get('longitude')
        if latitude and longitude:
            try:
                form.instance.latitude = float(latitude)
                form.instance.longitude = float(longitude)
            except ValueError:
                form.add_error(None, "Les coordonnées GPS ne sont pas valides.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Les coordonnées GPS sont requises.")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class affichage(ListView):
    model = Ville
    template_name = 'liste.html'
    def get_queryset(self):
        return Ville.objects.filter(user=self.request.user)
    
class detailView(TemplateView):
    template_name = 'detail.html'

class villeDetailView(DetailView):
    model = Ville
    template_name = 'detail.html'
    context_object_name = 'ville'   
    
class VilleUpdateView(UpdateView):
    model = Ville
    fields = ['nomV', 'nomQ', 'numM', 'descriptionV', 'imageQ', 'imageM', 'imageCH', 'latitude', 'longitude']  
    template_name = 'modifier.html' 
    context_object_name = 'ville'

    # Redirige vers la page de détails après la modification
    def get_success_url(self):
        return reverse_lazy('ville_detail', kwargs={'pk': self.object.pk})    
    
class VilleDeleteView(DeleteView):
    model = Ville
    success_url = reverse_lazy('affichage')  # Redirige après suppression
    template_name = 'ville_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "La ville a été supprimée avec succès.")
        return super().delete(request, *args, **kwargs)    

class clientsView(DetailView):
    model = Ville
    template_name = 'welcome/client.html'
    context_object_name = 'ville'  



class clientcreateView(CreateView):
    model = Client
    fields = ['nom', 'prenom', 'email', 'adresse', 'telephone', 'sexe']
    template_name = 'welcome/client.html'
    success_url = reverse_lazy('villes_list')  # URL de redirection après enregistrement
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupération de la ville à partir de l'URL
        ville_id = self.kwargs.get('ville_id')  # Récupère le 'ville_id' depuis l'URL
        ville = get_object_or_404(Ville, pk=ville_id)  # Trouve la ville par son ID ou renvoie 404
        context['ville'] = ville  # Ajoute la ville au contexte pour utilisation dans le template
        return context

