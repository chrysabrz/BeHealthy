# Generated by Django 4.0.1 on 2022-04-26 09:37

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_order_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='firstname',
            field=models.CharField(max_length=45, validators=[cart.models.test]),
        ),
    ]
