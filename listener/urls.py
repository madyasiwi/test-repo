"""
Wehbhook listener endpoints.
"""
from django.conf.urls import url
from listener.views import PushListener


urlpatterns = (
    url(r'^push/$', PushListener.as_view(), name='push'),
)
