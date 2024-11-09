from django.views.generic import ListView
from formation.models import Ville

class WelcomeView(ListView):
    model = Ville
    template_name = 'welcome/welcome.html'
    context_object_name = 'villes'  # Optionnel : spécifie le nom de l'objet passé au template
