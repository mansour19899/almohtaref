from django.template import loader
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from django.views.decorators.http import require_http_methods, require_GET, require_safe

@require_http_methods(["GET"])
def index(request, post_id=""):
    
    
    if post_id=="en":
                context = {
      'AboutUs':"ABOUT US",
      'ourProjects':"OUR PROJECTS",
      'Contactus':"CONTACT US",
      'languge':False,
      'hreflanguge':"../",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
    #   '':"",
        }  
    else:
        context = {
            'AboutUs':"در مورد ما",
            'ourProjects':"پروژه های اجرا شده",
            'Contactus':"تماس با ما",
            'languge':True,
            'hreflanguge':"en",
        }  

    return render(request, 'index.html', context)
    

