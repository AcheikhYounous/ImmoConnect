from django.shortcuts import render, get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm


#Ici c'est le views pour gerer les biens immobiliers: ajout, edition, suppression et listement

# ➕ Créer un bien
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('properties:property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})

# 📋 Lister les biens
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

# ✏️ Modifier un bien
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('properties:property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_form.html', {'form': form, 'edit_mode': True})

# 🗑️ Supprimer un bien
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('properties:property_list')
    return render(request, 'properties/property_confirm_delete.html', {'property': property})
