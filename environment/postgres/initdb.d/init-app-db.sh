#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER app PASSWORD 'app';
	CREATE DATABASE app;
	ALTER DATABASE app OWNER TO app;
	GRANT ALL PRIVILEGES ON DATABASE app TO app;
	GRANT ALL ON schema public TO app;
EOSQL