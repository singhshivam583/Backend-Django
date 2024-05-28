from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    chai_types_enums = [
        ('BT', 'Black Tea'),
        ('MT', 'Masala Tea'),
        ('ET', 'Elaichi Tea'),
        ('PT', 'Plain Tea'),
        ('GT', 'Ginger Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chaiImage/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_types_enums)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name