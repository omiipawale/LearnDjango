from django.db import models

class TaskList(models.Model):
    task = models.CharField(max_length=50)

    def __str__(self):
        return f"TaskName={self.task}"
