# Установки

## PostgresSQL
- Открыть psql console
- CREATE DATABASE travel_across_russia;
- CREATE USER travel_user WITH PASSWORD '1234';
- ALTER ROLE travel_user SET client_encoding TO 'utf8';
- ALTER ROLE travel_user SET default_transaction_isolation TO 'read committed';
- ALTER ROLE travel_user SET timezone TO 'UTC';
- GRANT ALL PRIVILEGES ON DATABASE travel_across_russia TO travel_user;
- \q

## -- для Django --
- manage.py makemigrations
- manage.py migrate
- manage.py createsuperuser
