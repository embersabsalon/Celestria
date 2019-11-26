from django.contrib.auth.models import User
from django.db import models


class AuthenticationToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=255, default=uuid4)
    expiration_date = models.DateTimeField()
