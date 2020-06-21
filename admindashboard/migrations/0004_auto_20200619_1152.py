# Generated by Django 3.0.2 on 2020-06-19 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_videofile'),
        ('admindashboard', '0003_addproductlist_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproductlist',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='discount_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='discount_percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='discount_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='product_image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Supplier'),
        ),
        migrations.AddField(
            model_name='addproductlist',
            name='videofile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]