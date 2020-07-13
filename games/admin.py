from django.contrib import admin
from .models import PLATFORM, DEVELOPER, PUBLISHER, GAME, GENRE

admin.site.register(PLATFORM)
admin.site.register(DEVELOPER)
admin.site.register(PUBLISHER)
admin.site.register(GAME)
admin.site.register(GENRE)
