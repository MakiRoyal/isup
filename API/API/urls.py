"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from isup.views import HomingPageView
from rest_framework import routers
from isup.views import DomainViewSet
from django.urls import include

router = routers.DefaultRouter()
router.register(r'domains', DomainViewSet)

urlpatterns = [
    path('', HomingPageView.as_view(), name='homePage'),
    path('api/', include((router.urls))),
    path("api/auth", include("rest_framework.urls", namespace="rest_framework")),

]


# GET /api/domains/  # Lister tous les domaines connus et leurs état (avec de la pagination si nécessaire).
# POST /api/domains/ -d '{"domain": "mdk.fr"}'  # Pour ajouter un nom de domaine (qui appartient à celui qui fait le POST).
# GET /api/domains/1/  # Afficher les informations du premier domaine.
# PUT /api/domains/1/  # Modifier le domaine 1, seulement autorisé si j'en suis propriétaire.
# DELETE /api/domains/1/  # Supprimer le domaine 1, seulement autorisé si j'en suis propriétaire.
# GET /api/checks/  # Lister toutes les vérifications qui ont été effectuées.
# GET /api/checks/?domain=1  # Lister toutes les vérifications effectuées pour le domaine 1.
# GET /api/checks/1  # Afficher le check d'id 1.
