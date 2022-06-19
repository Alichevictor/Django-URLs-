from django.contrib import admin
from django.urls import path
urlpatherns = [
 path('admin/', admin.site.urls),

]
path('', include('learning_logs.urls')),

"" Defines URL patherns for learning_logs.""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatherns =[
 #Home page
 path('', views.indexs.index, name='index'),


]
