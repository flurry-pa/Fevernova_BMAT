# Generated by Django 3.1 on 2020-08-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicWorkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iswc', models.CharField(default=None, max_length=30, verbose_name='ISWC')),
                ('title', models.CharField(default=None, max_length=30)),
                ('author_list', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
