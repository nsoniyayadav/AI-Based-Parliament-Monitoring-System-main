# serializers.py
from rest_framework import serializers
from .models import USPVideo, YouTubeVideo


class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['id', 'youtube_url', 'video_id', 'title', 'channel_name', 'transcript', 'summary_text', 'created_at']


class USPVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = USPVideo
        fields = '__all__'


class ProcessYouTubeRequestSerializer(serializers.Serializer):
    youtube_url = serializers.URLField(required=True)
    download_video = serializers.BooleanField(default=False)