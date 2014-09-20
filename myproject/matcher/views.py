from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import RequestContext, loader

from matcher.models import Hacker

# Create your views here.
def index(request):
   newest_hacker_list = Hacker.objects.all()[:5]
   context = {'newest_hacker_list' : newest_hacker_list}
   return render(request, 'matcher/index.html', context)

def detail(request, hacker_id):
    hacker = get_object_or_404(Hacker, pk=hacker_id)
    return render(request, 'matcher/detail.html', {'hacker': hacker})
