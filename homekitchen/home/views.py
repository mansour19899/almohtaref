from django.template import loader
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from django.views.decorators.http import require_http_methods, require_GET, require_safe

@require_http_methods(["GET"])
def index(request):
    
    context = {
      
    }
    return render(request, 'index.html', context)
    

