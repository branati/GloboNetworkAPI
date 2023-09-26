#!/bin/bash

# echo "Remove old list"
# rm loadfixtures_list_files.list

# NETWORKAPI_DATABASE_PASSWORD=SuperSecret NETWORKAPI_DATABASE_HOST=127.0.0.1 find ./networkapi/*/fixtures/ -type f -exec echo "Processing: {}" \; -exec python manage.py loaddata {}  \; > log_loadfixtures_output.txt 2> log_load_fixtures_errors.txt
# NETWORKAPI_DATABASE_PASSWORD=SuperSecret NETWORKAPI_DATABASE_HOST=127.0.0.1  find ./networkapi/*/fixtures/ -type f -exec bash -c 'echo "Processing: $0" && python manage.py loaddata $0' {} \; >> log_loadfixtures.txt 2>&1

# echo "Find fixtures files ..."
# find ./networkapi/*/fixtures/*.json -type f > loadfixtures_list_files.list

echo "Load loadfixtures_list_files.list and execute loadfixtures in django ..."
while IFS= read -r line; do
    echo $line
    # shellcheck disable=SC2129
    echo "-------------------------------------------------------" >> log_loadfixtures.log
    echo "Loading fixture: $line" >> log_loadfixtures.log
    NETWORKAPI_DATABASE_PASSWORD=SuperSecret NETWORKAPI_DATABASE_HOST=127.0.0.1 python manage.py loaddata "$line" >> log_loadfixtures.log 2>&1
    # echo "Press any key to continue..."
    # read -u 1 input
done < loadfixtures_list_files.list

# NETWORKAPI_DATABASE_PASSWORD=SuperSecret NETWORKAPI_DATABASE_HOST=127.0.0.1 python manage.py loaddata ./networkapi/ip/fixtures/initial_ipv4_eqpt.json >> log_loadfixtures.log 2>&1

# NETWORKAPI_DATABASE_PASSWORD=SuperSecret NETWORKAPI_DATABASE_HOST=127.0.0.1 python manage.py loaddata ./networkapi/ip/fixtures/initial_ipv4_eqpt.json >> log_loadfixtures.log 2>&1
