from django.urls import path
from right import views

urlpatterns = [
path('create-right', views.CreateRight.as_view()),
path('edit-right/<int:pk>',views.EditRight.as_view()),
path('delete-right/<int:pk>',views.DeleteRight.as_view())
]