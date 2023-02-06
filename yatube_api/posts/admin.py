from django.contrib import admin

from posts.models import Follow, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    search_fields = ('description', 'title')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')


admin.site.register(Group)
admin.site.register(Follow)
