from django.urls import path

from .import views

app_name='home'
urlpatterns = [

    path('', views.index , name='index'),
    # path('<int:post_id>', views.detail , name='detail'),
    # path('archive/<int:year>', views.archive , name='archive'), 
 
]
