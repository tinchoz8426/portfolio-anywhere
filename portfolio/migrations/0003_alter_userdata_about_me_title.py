# Generated by Django 4.1.7 on 2023-02-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolio_job_image_alter_portfolio_job_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='about_me_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
