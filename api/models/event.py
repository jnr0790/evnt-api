from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Date: {self.date}, Time: {self.time}"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'time': self.time
        }
