# Generated by Django 5.0.2 on 2024-02-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('academicyear', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('coursecode', models.CharField(max_length=100)),
                ('coursetitle', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'course_table',
            },
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facultyid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'faculty_table',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
