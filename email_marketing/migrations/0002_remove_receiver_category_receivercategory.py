# Generated by Django 4.2.7 on 2023-11-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_marketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='category',
        ),
        migrations.CreateModel(
            name='ReceiverCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ManyToManyField(to='email_marketing.category')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_marketing.receiver')),
            ],
        ),
    ]
