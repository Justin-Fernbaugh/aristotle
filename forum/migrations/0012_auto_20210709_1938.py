# Generated by Django 3.1.6 on 2021-07-10 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20210709_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='grouping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments_of_module', to='forum.assignmentmodule'),
        ),
    ]
