# Generated by Django 3.0.2 on 2020-06-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0005_auto_20200619_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproductlist',
            name='supplier_username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
