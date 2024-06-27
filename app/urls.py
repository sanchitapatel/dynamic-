from django.urls import path
from .views import *
urlpatterns=[
    #path("home/<int:pk>",home,name='home')
    path("combination/<path:pk>/<str:id>/<slug:pkid>/<int:idpk>",combination)
]