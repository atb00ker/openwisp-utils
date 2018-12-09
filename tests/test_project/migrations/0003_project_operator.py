# Generated by Django 2.1.3 on 2018-12-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0002_radiusaccounting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='test', max_length=30)),
                ('last_name', models.CharField(default='test', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='operator',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='test_project.Project'),
        ),
    ]
