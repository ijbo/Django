# Generated by Django 2.0.2 on 2018-04-25 18:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learningpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningpost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]