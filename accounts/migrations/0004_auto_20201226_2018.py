# Generated by Django 3.1.4 on 2020-12-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201226_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]