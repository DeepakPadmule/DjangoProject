# Generated by Django 2.1.7 on 2020-03-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grsApp', '0002_auto_20200325_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievancedetails',
            name='griev_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grsApp.Grievances'),
        ),
    ]
