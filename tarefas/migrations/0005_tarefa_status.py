# Generated by Django 2.0.2 on 2018-04-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_categoria_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='status',
            field=models.CharField(blank=True, choices=[('EA', 'Em Andamento'), ('C', 'Concluído'), ('CD', 'Cancelada')], default='', max_length=2, verbose_name='Status'),
        ),
    ]