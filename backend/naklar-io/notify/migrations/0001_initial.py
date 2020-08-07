# Generated by Django 3.0.6 on 2020-06-03 12:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationTimeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Montag'), (1, 'Dienstag'), (2, 'Mittwoch'), (3, 'Donnerstag'), (4, 'Freitag'), (5, 'Samstag'), (6, 'Sonntag')], max_length=13)),
                ('start_time', models.TimeField(verbose_name='Startzeit am Tag (in Sekunden)')),
                ('end_time', models.TimeField(verbose_name='Endzeit am Tag (in Sekunden)')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_push', models.BooleanField(default=False)),
                ('enable_mail', models.BooleanField(default=False)),
                ('notify_interval', models.DurationField(verbose_name=datetime.timedelta(seconds=300))),
                ('ranges_mode', models.CharField(choices=[('ALLOW', 'Während dieser Zeiten erlauben'), ('BLOCK', 'Während dieser Zeiten verbieten')], max_length=10)),
                ('ranges', models.ManyToManyField(to='notify.NotificationTimeRange')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
