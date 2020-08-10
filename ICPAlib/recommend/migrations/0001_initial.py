# Generated by Django 3.1 on 2020-08-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regi_id', models.CharField(blank=True, max_length=8, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('call_id', models.CharField(blank=True, max_length=11, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
    ]
