from django.db import models
from django.db.models import JSONField
import uuid


# =====================================================
# CITIZEN
# =====================================================

class Citizen(models.Model):

    username = models.CharField(max_length=150)

    password = models.CharField(max_length=150)

    aadhar = models.CharField(
        max_length=12,
        blank=True,
        default=''
    )

    pan = models.CharField(
        max_length=10
    )

    voter = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=100
    )

    dob = models.DateField()

    age = models.IntegerField()

    gender = models.CharField(
        max_length=10
    )

    category = models.CharField(
        max_length=50
    )

    cast = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    block = models.CharField(
        max_length=100
    )

    address = models.TextField()

    pincode = models.CharField(
        max_length=6
    )

    aadhar_file = models.FileField(
        upload_to='citizen_docs/'
    )

    pan_file = models.FileField(
        upload_to='citizen_docs/'
    )

    voter_file = models.FileField(
        upload_to='citizen_docs/'
    )

    profile_img = models.ImageField(
        upload_to='profile/'
    )

    citizen_id = models.CharField(
        max_length=16,
        unique=True,
        blank=True,
        null=True,
    )

    is_blocked = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):

        if not self.citizen_id:

            last_id = (
                Citizen.objects.count() + 1
            )

            self.citizen_id = (
                f"CTZ{last_id:06d}"
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f"{self.citizen_id} - "
            f"{self.username}"
        )


# =====================================================
# MP
# =====================================================

class MP(models.Model):

    username = models.CharField(max_length=150)

    password = models.CharField(max_length=150)

    aadhar = models.CharField(max_length=12)

    pan = models.CharField(max_length=10)

    voter = models.CharField(max_length=20)

    name = models.CharField(max_length=100)

    dob = models.DateField()

    age = models.IntegerField()

    gender = models.CharField(max_length=10)

    category = models.CharField(max_length=50)

    cast = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField()

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    block = models.CharField(max_length=100)

    address = models.TextField()

    pincode = models.CharField(max_length=6)

    aadhar_file = models.FileField(
        upload_to='citizen_docs/'
    )

    pan_file = models.FileField(
        upload_to='citizen_docs/'
    )

    voter_file = models.FileField(
        upload_to='citizen_docs/'
    )

    profile_img = models.ImageField(
        upload_to='profile/'
    )

    post_document = models.FileField(
        upload_to='mp_docs/'
    )

    post_id = models.CharField(
        max_length=50
    )

    mp_id = models.CharField(
        max_length=16,
        unique=True,
        blank=True,
        null=True,
    )

    user_login = JSONField(
        default=dict,
        blank=True
    )

    is_blocked = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):

        if not self.mp_id:

            last_id = (
                MP.objects.count() + 1
            )

            self.mp_id = (
                f"MP{last_id:06d}"
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f"{self.mp_id} - "
            f"{self.username}"
        )


# =====================================================
# MP FACE DETECTION
# =====================================================
class MPFaceDetection(models.Model):
    name = models.CharField(max_length=150)

    profile_image = models.ImageField(
        upload_to='mp_face_detection/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


# =====================================================
# MP ADMIN
# =====================================================
class MPAdminID(models.Model):
    mp = models.ForeignKey(
        MP,
        on_delete=models.CASCADE,
        related_name='admin_ids'
    )

    admin_id = models.CharField(
        max_length=150,
        unique=True,
    )

    username = models.CharField(max_length=150)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.admin_id} ({self.username})"


# =====================================================
# OFFLINE VIDEO
# =====================================================
class OfflineVideoUpload(models.Model):
    video_id = models.CharField(
        max_length=50,
        unique=True,
        editable=False
    )

    title = models.TextField()

    video_file = models.FileField(
        upload_to='videos/'
    )

    channel_name = models.CharField(max_length=200)

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.video_id:
            self.video_id = f"UP_{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.video_id} - {self.title}"


# =====================================================
# YOUTUBE VIDEO
# =====================================================
class YouTubeVideo(models.Model):
    youtube_url = models.URLField()

    video_id = models.CharField(
        max_length=50,
        unique=True,
    )

    title = models.TextField(blank=True)
    channel_name = models.CharField(
        max_length=255,
        blank=True,
    )

    video_file = models.FileField(
        upload_to='youtube_videos/',
        blank=True,
        null=True,
    )

    transcript = models.JSONField(
        default=list,
        blank=True,
    )

    summary_text = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.video_id} - {self.title}"


# =====================================================
# USP VIDEO
# =====================================================
class USPVideo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    video_uid = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
    )

    youtube_video = models.ForeignKey(
        YouTubeVideo,
        on_delete=models.CASCADE,
        related_name='usp_videos'
    )

    title = models.TextField()

    original_video_id = models.CharField(
        max_length=50,
        blank=True,
    )

    video_file = models.FileField(
        upload_to='usp_videos/'
    )

    transcript = JSONField(
        default=list,
        blank=True,
    )

    summary = models.TextField(
        blank=True,
    )

    highlights = JSONField(
        default=list,
        blank=True,
    )

    mp_speeches = JSONField(
        default=list,
        blank=True,
    )
    is_live = models.BooleanField(
    default=False
    )

    total_views = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    total_dislikes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    total_complaints = models.IntegerField(default=0)
    total_feedbacks = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='approved'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.video_uid:
            self.video_uid = "USP_" + uuid.uuid4().hex[:8].upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.video_uid} - {self.title}"


# =====================================================
# COMMENT
# =====================================================
class USPComment(models.Model):
    usp_video = models.ForeignKey(
        USPVideo,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    citizen = models.ForeignKey(
        Citizen,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    mp = models.ForeignKey(
        MP,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


# =====================================================
# VOTE
# =====================================================
class USPVote(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    usp_video = models.ForeignKey(
        USPVideo,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    citizen = models.ForeignKey(
        Citizen,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    mp = models.ForeignKey(
        MP,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    vote_type = models.CharField(
        max_length=10,
        choices=VOTE_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
class Meta:
    unique_together = (
        'usp_video',
        'citizen'
    )


# =====================================================
# COMPLAINT
# =====================================================
class USPComplaint(models.Model):
    usp_video = models.ForeignKey(
        USPVideo,
        on_delete=models.CASCADE,
        related_name='complaints'
    )

    citizen = models.ForeignKey(
        Citizen,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    mp = models.ForeignKey(
        MP,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


# =====================================================
# FEEDBACK
# =====================================================
class USPFeedback(models.Model):
    usp_video = models.ForeignKey(
        USPVideo,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    citizen = models.ForeignKey(
        Citizen,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    mp = models.ForeignKey(
        MP,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        default=5
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

