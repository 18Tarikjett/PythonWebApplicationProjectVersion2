from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

critical_level = [
    ('MIN','Minor'),
    ('MAJ','Major'),
    ('CRIT','Critical'),
]

class Post(models.Model): 
    ticket_problem = models.CharField(max_length=100)
    problem_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    ticket_level = models.CharField(max_length=20,
                                    choices=critical_level,
                                    default='MIN')
    ticket_employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_problem




