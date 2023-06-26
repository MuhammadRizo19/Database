# Generated by Django 4.2.1 on 2023-06-24 16:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_country_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
