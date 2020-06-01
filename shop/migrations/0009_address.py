# Generated by Django 2.2.4 on 2020-05-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('apartmentno', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=6)),
                ('category', models.CharField(choices=[('1', 'Category1'), ('2', 'Category2')], max_length=1)),
            ],
        ),
    ]