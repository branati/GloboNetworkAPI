# Generated by Django 4.2.4 on 2023-09-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45)),
            ],
            options={
                'db_table': 'object_type',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ObjectGroupPermissionGeneral',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('read', models.BooleanField()),
                ('write', models.BooleanField()),
                ('change_config', models.BooleanField()),
                ('delete', models.BooleanField()),
                ('object_type', models.ForeignKey(db_column='id_object_type', on_delete=django.db.models.deletion.DO_NOTHING, to='api_ogp.objecttype')),
                ('user_group', models.ForeignKey(db_column='id_user_group', on_delete=django.db.models.deletion.DO_NOTHING, to='grupo.ugrupo')),
            ],
            options={
                'db_table': 'object_group_permission_general',
                'abstract': False,
                'managed': True,
                'unique_together': {('user_group', 'object_type')},
            },
        ),
        migrations.CreateModel(
            name='ObjectGroupPermission',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('object_value', models.IntegerField(db_column='id_object')),
                ('read', models.BooleanField()),
                ('write', models.BooleanField()),
                ('change_config', models.BooleanField()),
                ('delete', models.BooleanField()),
                ('object_type', models.ForeignKey(db_column='id_object_type', on_delete=django.db.models.deletion.DO_NOTHING, to='api_ogp.objecttype')),
                ('user_group', models.ForeignKey(db_column='id_user_group', on_delete=django.db.models.deletion.DO_NOTHING, to='grupo.ugrupo')),
            ],
            options={
                'db_table': 'object_group_permission',
                'abstract': False,
                'managed': True,
                'unique_together': {('user_group', 'object_type', 'object_value')},
            },
        ),
    ]
