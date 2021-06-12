# Generated by Django 3.1.6 on 2021-06-12 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0013_auto_20210303_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='agreed',
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='disagreed',
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='stronged',
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='viewed',
        ),
        migrations.RemoveField(
            model_name='userwrapper',
            name='weaked',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserWrapper',
        ),
    ]