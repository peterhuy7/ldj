# Generated by Django 4.2.3 on 2023-07-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='congvc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tennv', models.CharField(max_length=800)),
                ('theloainv', models.CharField(max_length=1200)),
                ('congnangnv', models.CharField(max_length=1500)),
            ],
        ),
    ]
