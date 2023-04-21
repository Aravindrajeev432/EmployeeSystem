from django.urls import path

from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

from accounts import views


urlpatterns = [
    path('tesview', views.TestView.as_view()),
    path('list-members', views.ListMembers.as_view()),
    path('profile/<int:pk>', views.Profile.as_view()),
    path('register', views.CreateUser.as_view()),
    path('edit-user/<int:pk>', views.EditUser.as_view()),
    path('delete-user', views.DeleteUser.as_view()),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]