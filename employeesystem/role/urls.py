from django.urls import path
from role import views

urlpatterns = [
path('create-role',views.CreateRole.as_view(), name='create-role'),
path('list-role',views.ListRoles.as_view(), name='list-role'),
path('edit-role/<int:pk>',views.EditRole.as_view(), name='edit-role'),
path('delete-role/<int:pk>',views.DeleteRole.as_view(), name='delete-role'),
]