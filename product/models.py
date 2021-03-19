from django.db import models

# Create your models here.
class Product(models.Model): #product_category
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank = True, unique = True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image       = models.FileField(upload_to = 'products/', null = True, blank = True)
    featured    = models.BooleanField(default = False)
    active      = models.BooleanField(default = True)
    timestamp   = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title