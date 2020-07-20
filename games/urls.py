from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add/$(?i)', views.add_new_game_view, name='add_new_game'),
    url(r'^api/$(?i)', views.api_view, name='api'),
]
