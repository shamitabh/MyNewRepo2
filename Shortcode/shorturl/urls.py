from .views import ShortCodeAPIView, GetShortcodeStatsAPIView, GoToUrlAPIView
from django.urls import path

urlpatterns = [
    # api paths
    path('shorten', ShortCodeAPIView.as_view(), name='set_code'),
    path('<str:code>/stats', GetShortcodeStatsAPIView.as_view(), name='get_stats'),
    path('<str:code>', GoToUrlAPIView.as_view(), name='go_to_url'),
]
