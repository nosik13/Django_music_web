from django.contrib import admin

from see_app.models import Topic


# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('head', 'text', 'date_added')
    list_display_links = ('head', 'text')
    search_fields = ('head', 'text')


admin.site.register(Topic, TopicAdmin)
