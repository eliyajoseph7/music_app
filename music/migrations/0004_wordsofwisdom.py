# Generated by Django 3.0.2 on 2020-05-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200517_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordsOfWisdom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='static/img/scoan.png', upload_to='wisdom_images')),
                ('contents', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
