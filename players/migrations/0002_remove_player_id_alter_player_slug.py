# Generated by Django 4.0.4 on 2022-04-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]