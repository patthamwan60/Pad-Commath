from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('dto32/',views.decto32fp),
    path('dto64/',views.decto64fp),
    path('solve/',views.datasolve),
    path('difer/',views.differentiation),
    path('inte/',views.integration),
    path('root/',views.rootfinding),
]