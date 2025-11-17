#!/usr/bin/env bash
HOST="db-server"
USER="admin"
DB="desafio2"


psql "postgresql://$USER:admin123@$HOST:5432/$DB" -c "SELECT * FROM mensagens;"