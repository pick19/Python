# Generated by Django 2.0 on 2017-12-18 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Message')),
            ],
        ),
    ]
