# Generated by Django 3.0.2 on 2020-05-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_wordsofwisdom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordsofwisdom',
            name='image',
            field=models.ImageField(default='music_app/static/img/scoan.png', upload_to='wisdom_images'),
        ),
    ]
