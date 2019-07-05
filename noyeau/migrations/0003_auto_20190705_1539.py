# Generated by Django 2.2.2 on 2019-07-05 20:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('noyeau', '0002_auto_20190703_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='idclient',
            name='question_1',
            field=models.TextField(default='Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idclient',
            name='question_2',
            field=models.TextField(default='Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idclient',
            name='question_3',
            field=models.TextField(default='Text '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idclient',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
