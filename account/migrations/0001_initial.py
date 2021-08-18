# Generated by Django 3.2.6 on 2021-08-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=80, verbose_name='first name')),
                ('last_name', models.CharField(max_length=80, verbose_name='last name')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('profile_picture', models.ImageField(default='profile_pic.jpeg', upload_to='')),
                ('is_teacher', models.BooleanField()),
                ('about_me', models.TextField(null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
