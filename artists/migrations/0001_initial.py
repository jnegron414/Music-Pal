# Generated by Django 3.0.7 on 2020-06-06 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('website', models.URLField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
