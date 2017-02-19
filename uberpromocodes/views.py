from django.shortcuts import render
from .models import Promos
from django.utils import timezone
# Create your views here.
def home(request):
	posts = Promos.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'index.html', {'posts': posts})
