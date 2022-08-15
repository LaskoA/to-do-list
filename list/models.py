from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63,)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255,)
    date = models.DateField()
    deadline = models.DateField(blank=True, null=True,)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks",)

    class Meta:
        ordering = ["done", "date"]
