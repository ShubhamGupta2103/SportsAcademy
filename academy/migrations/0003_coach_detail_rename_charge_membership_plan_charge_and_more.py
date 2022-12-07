# Generated by Django 4.0.6 on 2022-08-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_membership_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('Experience', models.CharField(max_length=20)),
                ('About_coach', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='membership_plan',
            old_name='Charge',
            new_name='charge',
        ),
        migrations.RenameField(
            model_name='membership_plan',
            old_name='plan_name',
            new_name='plane_name',
        ),
    ]