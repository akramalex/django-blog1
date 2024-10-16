from django.db import models

# Create your models here.

from django.db import models

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)  # To mark requests as "read"
    created_on = models.DateTimeField(auto_now_add=True)  # Automatic timestamp

    def __str__(self):
        return f"Request from {self.name} - {'Read' if self.is_read else 'Unread'}"