from django.db import models
from django.contrib.auth.models import User

class System_Post(models.Model):
    user = models.ForeignKey(
        User, related_name="System_Post", on_delete=models.CASCADE
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )

