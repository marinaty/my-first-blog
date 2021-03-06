from django.shortcuts import render
from django.utils import timezone
from .models import Postear

# Create your views here.
def listar_publicaciones(request):
    posts = Postear.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_publicaciones.html', {'posts': posts})
