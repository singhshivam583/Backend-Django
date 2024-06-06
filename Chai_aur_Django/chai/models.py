from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

# One to Many 
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for Chai {self.chai.name}'
    
# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varity = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name

# One to One
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
