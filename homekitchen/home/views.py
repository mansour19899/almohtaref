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
      'langugee':"العربیه",
      'hreflanguage':"../",
      'dirction':"ltr",
      'ourcollections':"OUR COLLECTIONS",
      'ourcollectionsdetail':"<h5>If you are looking for modern, transitional or traditional design that are as exquisite as functional;Let Us Make Your Home Unique.A look you’re sure to love and the quality you deserve.</h5>",
      'textalign':"text-align:left;",
      'textalign':"text-align:left;",
      'textalign':"text-align:left;",
      'textalign':"text-align:left;",
      'textalign':"text-align:left;",
      


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
            'AboutUs':"لماذا المحترف",
            'ourProjects':"أعمال الشركة",
            'Contactus':"اتصل بنا",
            'languge':True,
            'langugee':"ENGLISH",
            'hreflanguage':"en",
            'dirction':"rtl",
            'textalign':"text-align:right;",
            'ourcollections':"كيف تطورت تصاميم المطبخ؟ ",
            'ourcollectionsdetail':"<h6>تصميم المطبخ الذي تراه كل يوم لم يكن موجود في الجزء الأول من القرن الماضي. إن ولادة العمارة الحديثة والتقدم التكنولوجي أثروا بشكل كبير على تصاميم المطبخ. حتى المنازل الكلاسيكية لديها مطابخ الحديثة التي هي بالطبع مصممة في تناغم مع البيئة الداخلية.   وقد زينت هذه المساحة الآن بأثاث عصري وأحدث الأجهزة التي لم يشاهدها أحد أبدا قبل نصف قرن. التجريب مع التخطيطات والمواد جلبت المزيد من التغييرات في هذا الفراغ. كل هذا يعني أن لديك مرونة أكبر لتصميم هذا المكان الحيوي من المنزل.</h6>;"

        }  

    return render(request, 'index.html', context)
    

