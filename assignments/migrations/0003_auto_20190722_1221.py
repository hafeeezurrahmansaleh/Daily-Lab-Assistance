# Generated by Django 2.2.3 on 2019-07-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_auto_20190719_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='feedback',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='givenmarks',
            field=models.FloatField(null=True),
        ),
    ]