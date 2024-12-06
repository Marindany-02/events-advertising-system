# urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),

    path('contact/', views.contact, name='contact'),

    path('login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),  # List all events
    path('manage_event/', views.manage_events, name='manage_event'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
    path('event_detail/<int:id>/', views.event_detail, name='event_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)