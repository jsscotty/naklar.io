# Generated by Django 3.0.4 on 2020-04-02 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roulette.Match', to_field='uuid'),
        ),
    ]
