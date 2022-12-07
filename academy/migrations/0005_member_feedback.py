# Generated by Django 4.0.6 on 2022-08-07 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('rating', models.IntegerField(default=1)),
                ('feedback_text', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
