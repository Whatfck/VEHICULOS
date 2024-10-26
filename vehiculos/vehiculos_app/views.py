from django.shortcuts import render,HttpResponseRedirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

def create_view(request):
    context = {}
    form = VehiculoForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, 'create_view.html', context)