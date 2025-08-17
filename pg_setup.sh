
#!/bin/bash

# Export environmental variables.
set -a
source .env
set +a

# Create the postgresql databases.
psql -p ${DB_PORT} -d postgres -c "DROP DATABASE ${DB_NAME};"
psql -p ${DB_PORT} -d postgres -c "CREATE DATABASE ${DB_NAME};"
psql -p ${DB_PORT} -d ${DB_NAME} -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';"

# To execute the tests, allow the user to have the permission to create databases.
psql -p ${DB_PORT} -d ${DB_NAME} -c "ALTER USER ${DB_USER} CREATEDB;"
