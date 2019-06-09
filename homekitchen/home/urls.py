from django.urls import path

from .import views

app_name='home'
urlpatterns = [

    path('', views.index , name='index'),
    path('<str:post_id>/', views.index , name='index'),
    # path('archive/<int:year>', views.archive , name='archive'), 
 
]
