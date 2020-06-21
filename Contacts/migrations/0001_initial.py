# Generated by Django 2.0.2 on 2020-06-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phoneNumber', models.IntegerField(max_length=12)),
            ],
        ),
    ]
