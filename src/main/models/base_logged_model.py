from main.middlewares.logging import local
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseLoggedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(local, 'user'):
            self.creator = local.user
        self.modified = timezone.now()
        return super(BaseLoggedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
