from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class FeedBack(models.Model):
    objects = None
    STATUSES = [("N", "New feedback"), ("P", "Feedback in process"), ("F", "Feedback is finished")]
    name = models.CharField(max_length=50, verbose_name="Full name")
    email = models.EmailField(max_length=50, verbose_name="User email")
    subject = models.CharField(max_length=50, verbose_name="Subject")
    message = models.TextField(verbose_name="Message", validators=[])
    status = models.CharField(max_length=1, choices=STATUSES, default="N", verbose_name="Feedback status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Last updated")

    class Meta:
        db_table = "feedback"
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.name
