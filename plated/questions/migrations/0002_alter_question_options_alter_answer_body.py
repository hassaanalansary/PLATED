# Generated by Django 5.0.7 on 2024-09-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['?']},
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
