# Generated by Django 3.0.8 on 2020-07-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Name', max_length=60)),
                ('city', models.CharField(max_length=300)),
                ('area', models.CharField(max_length=100)),
                ('pincode', models.PositiveIntegerField(max_length=6)),
                ('phone', models.PositiveIntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('insta', models.CharField(max_length=30)),
                ('feedback', models.TextField()),
            ],
        ),
    ]