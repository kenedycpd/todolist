# Generated by Django 3.0.3 on 2020-02-27 01:10

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tarefa')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('end_date', models.DateField(verbose_name='Data Final')),
                ('status', models.CharField(choices=[('EX', 'Em execução'), ('PD', 'Pendente'), ('CD', 'Concluida')], max_length=2, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
            ],
        ),
    ]
