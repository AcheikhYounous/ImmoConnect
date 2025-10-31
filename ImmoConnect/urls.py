"""
URL configuration for ImmoConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static # Pour servir les fichiers médias en développement
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Pour servir les fichiers statiques en développement
from . import settings # Importer les paramètres du projet
from django.conf.urls import handler404, handler403, handler500 # Importer les gestionnaires d'erreurs personnalisés tel que erreur 404, 403, 500
# from users.views import custom_403_view, custom_404_view, custom_500_view # Importer les vues personnalisées pour les erreurs

# handler404 = custom_404_view
# handler403 = custom_403_view
# handler500 = custom_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),  # URLs pour l'application des utilisateurs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
