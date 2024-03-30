from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friends')
    status = models.CharField(
        max_length=10, choices=[(
            'PENDING', 'Pending'), ('ACCEPTED', 'Accepted')])
