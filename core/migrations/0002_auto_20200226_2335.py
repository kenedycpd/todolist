# Generated by Django 3.0.3 on 2020-02-27 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TodoList'),
        ),
    ]
