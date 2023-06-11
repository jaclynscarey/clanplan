from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_index, name='index'),
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/join_family/', views.join_family, name='join_family'),
    path('events/<int:event_id>/assoc_attendee/<int:attendee_id>/', views.assoc_attendee, name='assoc_attendee'),
    path('events/<int:event_id>/unassoc_attendee/<int:attendee_id>/', views.unassoc_attendee, name='unassoc_attendee'),
]