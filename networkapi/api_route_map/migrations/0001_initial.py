# Generated by Django 4.2.4 on 2023-09-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipamento', '0001_initial'),
        ('api_list_config_bgp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentRouteMap',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('equipment', models.ForeignKey(db_column='id_equipment', on_delete=django.db.models.deletion.DO_NOTHING, to='equipamento.equipamento')),
            ],
            options={
                'db_table': 'equipment_route_map',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RouteMap',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('equipments', models.ManyToManyField(through='api_route_map.EquipmentRouteMap', to='equipamento.equipamento')),
            ],
            options={
                'db_table': 'route_map',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RouteMapEntry',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[('P', 'P'), ('D', 'D')], db_column='action', max_length=2)),
                ('action_reconfig', models.TextField(db_column='action_reconfig')),
                ('order', models.IntegerField(db_column='order')),
                ('list_config_bgp', models.ForeignKey(db_column='id_list_config_bgp', on_delete=django.db.models.deletion.DO_NOTHING, to='api_list_config_bgp.listconfigbgp')),
                ('route_map', models.ForeignKey(db_column='id_route_map', on_delete=django.db.models.deletion.DO_NOTHING, to='api_route_map.routemap')),
            ],
            options={
                'db_table': 'route_map_entry',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='equipmentroutemap',
            name='route_map',
            field=models.ForeignKey(db_column='id_route_map', on_delete=django.db.models.deletion.DO_NOTHING, to='api_route_map.routemap'),
        ),
    ]
