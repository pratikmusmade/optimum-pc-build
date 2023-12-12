# optimum-pc-build

Steps for developers to setup database locally:
(Until RDS instance is hosted)
- Install PostgreSQL
- Run the `/optimum-pc-build/sql/DB data optimum-pc-builds/optimum-pc-build-db.sql` file
OR
- Install psycopg2
- Create tables manually using the `/optimum-pc-build/sql/DB data optimum-pc-builds/optimum-pc-build-db.sql` file
- Load data using `/optimum-pc-build/sql/DB data optimum-pc-builds/insert_json_to_postgres.py` script. Initially scrapped data is stored in JSON files