# Generated by Django 4.1.4 on 2022-12-21 15:27

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Student',
                'ordering': ['roll_no'],
            },
            managers=[
                ('student_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Proxy_Student',
            fields=[
            ],
            options={
                'db_table': 'Proxy_Student',
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.student',),
            managers=[
                ('proxy_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]