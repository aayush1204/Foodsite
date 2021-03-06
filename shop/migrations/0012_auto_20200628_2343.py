# Generated by Django 3.0.7 on 2020-06-28 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0011_auto_20200621_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='OrderSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_id', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('apartmentno', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=6)),
                ('is_completed', models.BooleanField(default=False)),
                ('total_amount', models.IntegerField(default=0)),
                ('items', models.ManyToManyField(to='shop.Cart')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Supplier')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
