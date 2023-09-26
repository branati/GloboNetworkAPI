# Generated by Django 4.2.4 on 2023-09-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipamento', '0001_initial'),
        ('vlan', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vrf',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('vrf', models.TextField(db_column='vrf', max_length=45)),
                ('internal_name', models.TextField(db_column='internal_name', max_length=45)),
            ],
            options={
                'db_table': 'vrf',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VrfVlanEquipment',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('equipment', models.ForeignKey(db_column='id_equipment', on_delete=django.db.models.deletion.DO_NOTHING, to='equipamento.equipamento')),
                ('vlan', models.ForeignKey(db_column='id_vlan', on_delete=django.db.models.deletion.DO_NOTHING, to='vlan.vlan')),
                ('vrf', models.ForeignKey(db_column='id_vrf', on_delete=django.db.models.deletion.DO_NOTHING, to='api_vrf.vrf')),
            ],
            options={
                'db_table': 'vrf_vlan_eqpt',
                'abstract': False,
                'managed': True,
                'unique_together': {('vlan', 'equipment')},
            },
        ),
        migrations.CreateModel(
            name='VrfEquipment',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('internal_name', models.TextField(db_column='internal_name', max_length=45)),
                ('equipment', models.ForeignKey(db_column='id_equipment', on_delete=django.db.models.deletion.DO_NOTHING, to='equipamento.equipamento')),
                ('vrf', models.ForeignKey(db_column='id_vrf', on_delete=django.db.models.deletion.DO_NOTHING, to='api_vrf.vrf')),
            ],
            options={
                'db_table': 'vrf_eqpt',
                'abstract': False,
                'managed': True,
                'unique_together': {('vrf', 'equipment')},
            },
        ),
    ]
