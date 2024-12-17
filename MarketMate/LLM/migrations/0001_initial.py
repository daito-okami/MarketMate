# Generated by Django 5.1.2 on 2024-11-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('BAKERY', 'Bakery & Pastries'), ('DAIRY', 'Dairy & Eggs'), ('MEAT', 'Meat & Poultry'), ('SEAFOOD', 'Fish & Seafood'), ('FRUITS', 'Fruits & Vegetables'), ('PANTRY', 'Pantry & Dry Goods'), ('FROZEN', 'Frozen Foods'), ('SNACKS', 'Snacks & Confectionery'), ('BEVERAGES', 'Beverages'), ('DELI', 'Deli & Prepared Foods'), ('CANNED', 'Canned & Preserved'), ('CONDIMENTS', 'Condiments & Sauces'), ('GRAINS', 'Grains & Pasta'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('original_price', models.FloatField()),
                ('sell_percentage', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('two_for_one', models.BooleanField(default=False)),
                ('market_name', models.CharField(max_length=20)),
            ],
        ),
    ]