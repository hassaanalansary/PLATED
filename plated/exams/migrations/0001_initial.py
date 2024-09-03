# Generated by Django 5.0.7 on 2024-09-03 20:56

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('subjects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('solved_at', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, default=datetime.timedelta(seconds=3600), null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', related_query_name='exam', to='subjects.chapter')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', related_query_name='exam', to='subjects.lesson')),
                ('questions', models.ManyToManyField(to='questions.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', related_query_name='exam', to='users.student')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', related_query_name='exam', to='subjects.subject')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', related_query_name='exam', to='subjects.unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
            options={
                'unique_together': {('student', 'exam', 'answer')},
            },
        ),
    ]
