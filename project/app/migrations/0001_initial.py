# Generated by Django 2.0.6 on 2018-07-09 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=128)),
                ('follower_count', models.IntegerField()),
                ('follow_count', models.IntegerField()),
                ('descriptionn', models.TextField()),
            ],
        ),
    ]
