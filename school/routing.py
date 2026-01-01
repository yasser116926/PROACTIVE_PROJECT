from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/school/vcr/(?P<classroom_id>\w+)/$', consumers.SchoolConsumer.as_asgi()),
    # Uncomment the next line only if VCRConsumer exists
    # re_path(r'ws/vcr/$', consumers.VCRConsumer.as_asgi()),
]
