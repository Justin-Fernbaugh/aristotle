# Generated by Django 3.1.6 on 2021-06-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20210612_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWrapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_teacher', models.BooleanField()),
            ],
        ),
    ]
