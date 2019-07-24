-- User: twin
-- DROP USER twin;

CREATE USER twin WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  CREATEDB
  NOCREATEROLE;

-- Database: twin
-- DROP DATABASE twin;

CREATE DATABASE twin
    WITH
    OWNER = twin
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.utf8'
    LC_CTYPE = 'ru_RU.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
