from django.urls import path

from . import views

urlpatterns = [
    path('<int:root_id>', views.details, name="detail")
  ]
