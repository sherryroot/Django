# Generated by Django 2.2.1 on 2019-06-29 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool_test', '0007_orders_af_orders_td_orders_tm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders_af',
        ),
        migrations.DeleteModel(
            name='Orders_td',
        ),
        migrations.DeleteModel(
            name='Orders_tm',
        ),
    ]
