# Generated by Django 2.2 on 2021-05-30 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0046_auto_20210530_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='auteur',
            field=models.ForeignKey(on_delete='models.DO_NOTHING', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='post',
            field=models.ForeignKey(on_delete='models.CASCADE', to='communitymanager.Post'),
        ),
        migrations.AlterField(
            model_name='communaute',
            name='createur',
            field=models.ForeignKey(on_delete='models.DO_NOTHING', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='auteur',
            field=models.ForeignKey(on_delete='models.DO_NOTHING', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='priorite',
            field=models.ForeignKey(on_delete='models.DO_NOTHING', to='communitymanager.Priorite'),
        ),
    ]
