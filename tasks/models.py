from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10)

    class Meta:
        db_table = "task"
        managed = True
    
    def __str__(self):
        return self.title