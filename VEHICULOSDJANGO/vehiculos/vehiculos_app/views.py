from django.shortcuts import render,HttpResponsePermanentRedirect,get_object_or_404

# Create your views here.


# relative import of forms
from .models import vehicle
from .forms import VehicleForm

def create_view(request):
    context ={}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponsePermanentRedirect("/")
    
    context['form']= form
    return render(request, "create_view.html", context)