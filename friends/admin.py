from django.contrib import admin

from .models import FriendList, FriendRequest


class FriendListAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    list_display = ["user"]
    search_fields = ["user"]
    readonly_fields = ["user"]

    class Meta:
        model = FriendList


admin.site.register(FriendList, FriendListAdmin)


class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ["sender", "receiver"]
    list_display = ["is_active", "sender", "receiver"]
    search_fields = ["sender__email", "receiver__email"]

    class Meta:
        model = FriendRequest


admin.site.register(FriendRequest, FriendRequestAdmin)
