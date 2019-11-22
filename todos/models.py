from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('todos:todo_details', kwargs={"id": self.id})
    def get_delete_url(self):
        return reverse('todos:todo_delete', kwargs={"id": self.id})
    def get_edit_url(self):
        return reverse('todos:todo_edit', kwargs={"id": self.id})