#!/bin/bash

echo ================ Exclude all migrations files in the directories =====================
find ./networkapi/*/migrations/ -type f -exec rm -f {} \;
cd dbmigrate
db-migrate up
cd ..

echo  ======================= Executing Make Migrations ===================================
python manage.py makemigrations
python manage.py makemigrations api_aws
python manage.py makemigrations grupo
python manage.py makemigrations rack
python manage.py makemigrations equipamento
python manage.py makemigrations roteiro
python manage.py makemigrations ambiente
python manage.py makemigrations api_vrf
python manage.py makemigrations filter
python manage.py makemigrations vlan
python manage.py makemigrations tipoacesso

python manage.py makemigrations api_asn
python manage.py makemigrations api_list_config_bgp


python manage.py makemigrations ip
python manage.py makemigrations api_route_map
python manage.py makemigrations api_peer_group
python manage.py makemigrations api_neighbor

python manage.py makemigrations api_network

python manage.py makemigrations api_ogp

python manage.py makemigrations api_pools

python manage.py makemigrations healthcheckexpect
python manage.py makemigrations requisicaovips
python manage.py makemigrations blockrules
python manage.py makemigrations api_vip_request

python manage.py makemigrations semaforo

python manage.py makemigrations snippets

python manage.py makemigrations system

python manage.py makemigrations usuario

echo  ======================= Executing Migrate ===================================
python manage.py migrate
# python manage.py migrate api_aws
# python manage.py migrate grupo
# python manage.py migrate equipamento
# python manage.py migrate rack

# python manage.py migrate api_vrf

