# Generated by Django 2.2 on 2021-05-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0033_communaute_ferme'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='collant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
