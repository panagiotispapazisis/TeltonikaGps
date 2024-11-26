# models.py
from django.db import models

class GpsData(models.Model):
    message = models.JSONField()  # Αποθηκεύει τα δεδομένα του TCP server ως JSON
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"GPS Data {self.timestamp}"