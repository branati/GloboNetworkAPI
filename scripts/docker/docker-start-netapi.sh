#
# Script to run Network API on a docker container
#

# Time to sleep before retrying to talk to database container
SLEEP_TIME=5

# Maximum number of retries on database container
MAX_RETRIES=30

# Network API pid file path
PIDFILE=/var/run/netapi_main.pid

# Control variable to check if the database container is ready
DB_READY=0


#
# Script begin
#

python --version
source /venv/bin/activate

echo VIRTUAL_ENV= ${VIRTUAL_ENV}
echo VIRTUAL_ENV= $VIRTUAL_ENV
echo "Starting netapi_app ..."

# Waits for database container to be ready
#if [ "$NETWORKAPI_DATABASE_HOST" -eq "localhost" ]; then
#    for i in $(seq 1  ${MAX_RETRIES}); do
#    echo "localhosttttttttttttttttt"
#    mysql -u root -h ${NETWORKAPI_DATABASE_HOST} -e 'DROP DATABASE IF EXISTS networkapi;'
#
#    if [ "$?" -eq "0" ]; then
#        echo "Dropping old networkapi database"
#        DB_READY=1;
#        break;
#    fi
#
#    echo "DB not ready. Trying again in ${SLEEP_TIME} seconds."
#    sleep ${SLEEP_TIME}
#    echo "Retrying ${i}.."
#    done
#
#
#    # Exits if we can not connect to database container
#    if [ "$DB_READY" -eq "0" ]; then
#    echo "Fatal error: Could not connect to DB"
#    exit 1;
#    fi
#fi

echo "Creating networkapi database"
# echo NETWORKAPI_DATABASE_HOST = ${NETWORKAPI_DATABASE_HOST}
mysql -u root -h "${NETWORKAPI_DATABASE_HOST}"  -p"${NETWORKAPI_DATABASE_PASSWORD}" -e 'CREATE DATABASE IF NOT EXISTS networkapi;'

# Running database migrations if exists
echo "Running database migrations if exists"
# ls /netapi
# cd /netapi/dbmigrate; db-migrate up --show-sql
echo "Running simple-db-migrate with older variable table"
cd /netapi/dbmigrate; DEBUG=db-migrate:* db-migrate up

echo "Running Django Migrate"
cd /netapi/; python manage.py migrate


echo "Loading base Network API data into database"
# mysql -u root -h ${NETWORKAPI_DATABASE_HOST} networkapi < /netapi/dev/load_example_environment.sql


# Discovering SDN controller
REMOTE_CTRL=$(nslookup ${NETWORKAPI_SDN_CTRL} | grep Address | tail -1 | awk '{print $2}')
echo "$REMOTE_CTRL  odl.controller" >> /etc/hosts
echo "Found SDN controller: ${REMOTE_CTRL}"

echo "Starting gunicorn using supervisord"
supervisord -c /netapi/scripts/docker/netapi_supervisord.conf
sleep 5

echo "Processes starteds!"
ps aux

echo "SupervisorD logs"
tail -50 /tmp/supervisord.log

echo "Gunicorn logs"

tail -50 /tmp/gunicorn-networkapi_error.log
# tail -50 /tmp/networkapi.log
echo "Network API logs"
# cat /tmp/supervisord.log
# tail -f netapi stdout
supervisorctl tail -f netapi stdout

