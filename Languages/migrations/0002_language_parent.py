# Generated by Django 2.2 on 2019-07-06 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Languages.Language'),
        ),
    ]
