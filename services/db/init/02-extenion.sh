#!/bin/bash

set -o errexit

main() {
  add_extension  
}

add_extension() { 
  psql --username "postgres" -c 'CREATE EXTENSION "uuid-ossp";' "$FILLA_DB_DATABASE"
}

main "$@"