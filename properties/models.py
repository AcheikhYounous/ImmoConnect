import os
from datetime import datetime
from django.utils.text import slugify
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# 🔤 Fonction pour renommer automatiquement les images uploadées
def property_image_path(instance, filename):
    # On récupère l'extension du fichier (.jpg, .png, etc.)
    ext = filename.split('.')[-1]
    
    # On crée un nom de base propre basé sur le titre du bien
    base_name = slugify(instance.title)
    
    # On ajoute un timestamp pour éviter les doublons
    filename = f"{base_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    
    # On place tout ça dans le dossier 'properties/'
    return os.path.join('properties/', filename)


# 🏡 Modèle Property (Bien immobilier)
class Property(models.Model):
    CATEGORY_CHOICES = [
        ('house', 'Maison'),
        ('apartment', 'Appartement'),
        ('land', 'Terrain'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    # 🔽 Ici on change juste la ligne suivante :
    main_image = models.ImageField(upload_to=property_image_path, blank=True, null=True)

    def __str__(self):
        return self.title


# 🧹 Supprimer l'image du disque si on supprime le bien
@receiver(post_delete, sender=Property)
def delete_property_image(sender, instance, **kwargs):
    if instance.main_image:
        instance.main_image.delete(False)
