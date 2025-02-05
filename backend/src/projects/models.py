from django.db import models

from accounts.models import Customer


# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    TYPE_CHOICES = {
        'CP': 'Customer project',
        'IP': 'Internal project'
    }
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default=TYPE_CHOICES.get('CP'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title


class Task(models.Model):
    LEVEL_CHOICES = [
        (1, 'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
        (4, 'level 4'),
        (5, 'level 5'),
    ]
    STATUS_CHOICES = [
        ('TODO', 'todo'),
        ('ONGOING', 'ongoing'),
        ('COMPLETED', 'completed'),
        ('CEO_APPROVED', 'CEO approved'),
    ]
    PRIORITY_CHOICES = [
        ('LESS', 'less priority'),
        ('HIGH', 'high priority'),
        ('NECESSARY', 'necessary'),
        ('VITAL', 'vital'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1, null=True, blank=True)
    stage = models.CharField(max_length=30, null=True, blank=True)
    attribution_to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='attributions', null=True,
                                       blank=True)
    contributor = models.ManyToManyField(Customer, related_name='contributions', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO', null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='task_files/', blank=True, null=True)
