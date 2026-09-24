from django.contrib import admin

from .models import (
    Citizen,
    USPVideo,
    OfflineVideoUpload,
    MP,
    MPFaceDetection,
    MPAdminID,
    YouTubeVideo,
    USPComment,
    USPVote,
    USPComplaint,
    USPFeedback,
)


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'city', 'state', 'is_blocked')
    search_fields = ('username', 'name', 'email', 'aadhar')


@admin.register(MP)
class MPAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'post_id', 'is_blocked')
    search_fields = ('username', 'name', 'email', 'post_id')


@admin.register(USPVideo)
class USPVideoAdmin(admin.ModelAdmin):
    list_display = ('video_uid', 'title', 'status', 'is_active', 'created_at')
    search_fields = ('video_uid', 'title')
    list_filter = ('status', 'is_active')


@admin.register(OfflineVideoUpload)
class OfflineVideoUploadAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'channel_name', 'uploaded_at')
    search_fields = ('video_id', 'title', 'channel_name')


@admin.register(MPFaceDetection)
class MPFaceDetectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(MPAdminID)
class MPAdminIDAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'username', 'mp', 'is_active', 'created_at')
    search_fields = ('admin_id', 'username')
    list_filter = ('is_active',)


admin.site.register(YouTubeVideo)
admin.site.register(USPComment)
admin.site.register(USPVote)
admin.site.register(USPComplaint)
admin.site.register(USPFeedback)

