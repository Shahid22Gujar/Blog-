# Generated by Django 4.0.2 on 2022-02-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
