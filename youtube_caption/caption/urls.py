from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caption_generator/<int:pk>', views.caption_generator, name='caption_generator'),
]