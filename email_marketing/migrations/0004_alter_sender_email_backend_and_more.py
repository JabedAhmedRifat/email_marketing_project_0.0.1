# Generated by Django 4.2.7 on 2023-11-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_marketing', '0003_receiver_email_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sender',
            name='EMAIL_BACKEND',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sender',
            name='EMAIL_USE_TLS',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
