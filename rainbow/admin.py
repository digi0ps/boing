from django.contrib import admin
from rainbow.models import story


class story_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'story', 'createdTime',)


admin.site.register(story, story_admin)
