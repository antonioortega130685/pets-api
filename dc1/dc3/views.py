from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import Pet
from django.views.generic import ListView

# Create your views here.
def Vista(request):
    return HttpResponse('Hola che')

class Profile(ListView):

	model = Pet
	template_name = 'owner.html'

	def get_queryset(self):
		return Pet.objects.all()
    
