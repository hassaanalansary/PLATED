# Generated by Django 5.0.7 on 2024-08-16 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0002_alter_answer_body'),
        ('subjects', '0009_lesson_grade_lesson_semester'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('solved_at', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.chapter')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.lesson')),
                ('questions', models.ManyToManyField(to='questions.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.unit')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
            options={
                'unique_together': {('student', 'exam', 'answer')},
            },
        ),
    ]
