# Generated by Django 3.1.7 on 2021-02-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210226_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='image',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]