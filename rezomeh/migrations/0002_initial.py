# Generated by Django 5.1.5 on 2025-01-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezomeh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('expertise', models.CharField(max_length=155)),
                ('Address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=155)),
                ('freelance_status', models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available'), ('busy', 'Busy')], default='not_available', max_length=15)),
            ],
        ),
    ]
