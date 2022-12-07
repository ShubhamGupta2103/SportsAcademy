# Generated by Django 4.0.6 on 2022-08-04 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sport_detail',
            fields=[
                ('Sport_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Sport_type', models.CharField(default='Indoor', max_length=30)),
                ('Description', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
