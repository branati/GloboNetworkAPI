# Generated by Django 4.2.4 on 2023-09-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRoteiro',
            fields=[
                ('id', models.AutoField(db_column='id_tipo_roteiro', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=40, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'tipo_roteiro',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id', models.AutoField(db_column='id_roteiros', primary_key=True, serialize=False)),
                ('roteiro', models.CharField(max_length=50)),
                ('descricao', models.CharField(blank=True, max_length=100)),
                ('tipo_roteiro', models.ForeignKey(db_column='id_tipo_roteiro', on_delete=django.db.models.deletion.DO_NOTHING, to='roteiro.tiporoteiro')),
            ],
            options={
                'db_table': 'roteiros',
                'abstract': False,
                'managed': True,
            },
        ),
    ]