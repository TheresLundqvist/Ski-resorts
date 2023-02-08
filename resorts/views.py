from django.shortcuts import render
from django.views import generic
from .models import Resort


class ResortList(generic.ListView):
    model = Resort
    queryset = Resort.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

