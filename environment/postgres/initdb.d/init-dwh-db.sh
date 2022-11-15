#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER dwh PASSWORD 'dwh';
	CREATE DATABASE dwh;
	ALTER DATABASE dwh OWNER TO dwh;
	GRANT ALL PRIVILEGES ON DATABASE dwh TO dwh;
	GRANT ALL ON schema public TO dwh;
EOSQL