from django.db import models

# Create your models here.
class Article(models.Model):
    FOOD_CATEGORIES = [
        ('BAKERY', 'Bakery & Pastries'),
        ('DAIRY', 'Dairy & Eggs'),
        ('MEAT', 'Meat & Poultry'),
        ('SEAFOOD', 'Fish & Seafood'),
        ('FRUITS', 'Fruits & Vegetables'),
        ('PANTRY', 'Pantry & Dry Goods'),
        ('FROZEN', 'Frozen Foods'),
        ('SNACKS', 'Snacks & Confectionery'),
        ('BEVERAGES', 'Beverages'),
        ('DELI', 'Deli & Prepared Foods'),
        ('CANNED', 'Canned & Preserved'),
        ('CONDIMENTS', 'Condiments & Sauces'),
        ('GRAINS', 'Grains & Pasta'),
        ('OTHER', 'Other')
    ]

    MARKET_NAMES = [
        ('BILLA', 'BILLA'),
        ('FANTASITCO', 'FANTASTICO'),
        ('DAR', 'DAR'),
        ('LIDL', 'LIDL'),
        ('KAUFLAND', 'KAUFLAND')
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(
        max_length=20,
        choices=FOOD_CATEGORIES,
        default='OTHER')

    original_price = models.FloatField()
    sell_percentage = models.IntegerField()
    discounted_price = models.IntegerField()
    img = models.ImageField()
    two_for_one = models.BooleanField(default=False)
    market_name = models.CharField(max_length=20)


