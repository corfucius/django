# Generated by Django 2.1.2 on 2018-10-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]