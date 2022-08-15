# Generated by Django 4.1 on 2022-08-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('done', models.BooleanField()),
                ('tags', models.ManyToManyField(to='list.tag')),
            ],
        ),
    ]
