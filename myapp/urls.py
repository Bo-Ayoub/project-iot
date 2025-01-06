from django.urls import path
from .views import UserListView, UserDetailView, LoginView,DailyMaxValuesView,CurrentMaxValuesView,UsersWithRole1
from . import views

urlpatterns = [
    path('', views.receive_temperature_humidity, name='home'),
    path('post', views.receive_temperature_humidity, name='post_temperature_humidity'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
# Rolee Endpoints
    path('roles/', views.RoleListView.as_view(), name='role-list'),
    path('roles/<int:id>/', views.RoleDetailView.as_view(), name='role-detail'),

    # Temperature Endpoints
    path('temperatures/', views.TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:id>/', views.TemperatureDetailView.as_view(), name='temperature-detail'),

    # Action Endpoints
    path('actions/', views.ActionListView.as_view(), name='action-list'),
    path('actions/<int:id>/', views.ActionDetailView.as_view(), name='action-detail'),
    path('actions/user/<int:user_id>/', views.UserActionsView.as_view(), name='user-actions'),

    # Incident Endpoints
    path('incidents/', views.IncidentListView.as_view(), name='incident-list'),
    path('incidents/<int:id>/', views.IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/user/<int:user_id>/', views.UserIncidentsView.as_view(), name='user-incidents'),
    path('incidents/temperature/<int:temperature_id>/', views.TemperatureIncidentsView.as_view(), name='temperature-incidents'),
    path('incidents/resolved/', views.ResolvedIncidentsView.as_view(), name='resolved-incidents'),
    path('incidents/unresolved/', views.UnresolvedIncidentsView.as_view(), name='unresolved-incidents'),

    # Commentaire Endpoints
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:id>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comments/incident/<int:incident_id>/', views.IncidentCommentsView.as_view(), name='incident-comments'),
    path('comments/user/<int:user_id>/', views.UserCommentsView.as_view(), name='user-comments'),

    path('incidents/user/<int:user_id>/', views.UserIncidentsView.as_view(), name='user-incidents'),
    path('incidents/temperature/<int:temperature_id>/', views.TemperatureIncidentsView.as_view(),
         name='temperature-incidents'),
    path('comments/incident/<int:incident_id>/', views.IncidentCommentsView.as_view(), name='incident-comments'),
    path('comments/user/<int:user_id>/', views.UserCommentsView.as_view(), name='user-comments'),
    path('daily-max/', DailyMaxValuesView.as_view(), name='daily-max'),
    path('current-value/',CurrentMaxValuesView.as_view(),name='current-value'),
    path('users/role1/',UsersWithRole1.as_view(),name='users_with_role_1'),
]
