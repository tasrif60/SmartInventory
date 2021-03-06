# Generated by Django 3.0.3 on 2020-03-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('unit', models.IntegerField(max_length=50)),
                ('in_stock', models.FloatField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='InventoryList',
        ),
    ]
