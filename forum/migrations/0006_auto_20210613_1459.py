# Generated by Django 3.1.6 on 2021-06-13 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_remove_submission_earned_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='total_points',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_points', models.FloatField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_of_assignment', to='forum.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_of_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
