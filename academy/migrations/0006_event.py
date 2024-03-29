# Generated by Django 4.0.6 on 2022-08-08 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_member_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.TextField()),
                ('event_venue', models.CharField(max_length=180)),
                ('event_pic', models.FileField(default='', upload_to='academy/picture')),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
