# Generated by Django 5.0.4 on 2024-04-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message',
        ),
        migrations.AddField(
            model_name='chat',
            name='image',
            field=models.ImageField(default='-', upload_to='images/'),
            preserve_default=False,
        ),
    ]
