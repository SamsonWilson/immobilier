# formation/urls.py
from django.urls import path
# from AT.AT import settings
from . import views
from django.conf.urls.static import static# Import relatif de views.py

urlpatterns = [
    # path('', views.exemple_view, name='exempl'),
    path('', views.IndexView.as_view(), name='IFadmin'),
    path('ville', views.FormView.as_view(), name='ville'),
    path('affichage', views.affichage.as_view(), name='affichage'),
    path('ville/<int:pk>/', views.villeDetailView.as_view(), name='ville_detail'),
    path('ville/<int:pk>/modifier/', views.VilleUpdateView.as_view(), name='ville_modifier'),
    path('ville/<int:pk>/supprimer/', views.VilleDeleteView.as_view(), name='ville_supprimer'),
    # path('welcome', views.welcomeView.as_view(), name='welcome'),
    
    # partie clients

    
    # path('clients/<int:pk>/', views.clientsView.as_view(), name='clients'),
    path('clients/add/<int:ville_id>/', views.clientcreateView.as_view(), name='client_add'),


    # path('creer-ville/', views.CreerVilleView, name='creer_ville'),
    # path('', IndexView.as_view(), name='index'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
