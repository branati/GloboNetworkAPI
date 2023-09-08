#!/bin/bash

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
echo  ======================= Executing Migrate ===================================
python manage.py migrate
# python manage.py migrate api_aws
# python manage.py migrate grupo
# python manage.py migrate equipamento
# python manage.py migrate rack

# python manage.py migrate api_vrf

