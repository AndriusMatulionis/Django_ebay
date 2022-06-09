from django.db import models

class Scrape(models.Model):
    
    #nr = models.IntegerField(auto_created=False, serialize=False, verbose_name='ID')
    item = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    seller = models.CharField(max_length=50)
    url = models.CharField(max_length=250)
    

    class Meta:
        db_table = 'scraped'

