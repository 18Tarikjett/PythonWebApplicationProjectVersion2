from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

critical_level = [
    ('MIN','Minor'),
    ('MAJ','Major'),
    ('CRIT','Critical'),
]


posts = [
    {
        'author': 'Tarik Ozturk',
        'title':'Help Desk ticket service for hardware and software.',
        'content':'This web page is for all employees that may have encountered issues with their hardware or software',
        'date_posted':'August 22nd 2023'
    },

    {
        'author': 'Tarik Ozturk',
        'title':'Criteria for the tickets.',
        'content':
        """
        The criteria for the tickets are as follows: 
            Minor - The least critical level, the problem is not very serious. 
            Major - The problem needs to be solved as soon as possible. 
            Critical - The problem is a top priority and must be immediately resolved.
        """,
        'date_posted':'August 22nd 2023'

    }
]




