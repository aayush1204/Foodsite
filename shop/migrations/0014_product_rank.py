# Generated by Django 2.2.4 on 2020-08-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_refunds_refund_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]