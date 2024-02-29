# Generated by Django 5.0.2 on 2024-02-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=120)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
