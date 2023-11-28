from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    surename = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.surename}, {self.first_name}"

class Tasks(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    due_date = models.DateField(null=True)
    status = models.BooleanField(default=False)
    preority = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.owner}, {self.title}, {self.due_date}, {self.preority}, {self.created_at}"
