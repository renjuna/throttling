from django.conf.urls import url,include
from .views import ExampleView
urlpatterns = [
    url(r'^throttle/$',ExampleView.as_view(),name='throttle'),
    ]
