CREATE USER sso WITH PASSWORD 'sso' CREATEDB;
CREATE DATABASE test
WITH 
    OWNER = sso
    ENCODING = 'UTF8';
CREATE table IF NOT EXISTS test (id int, name varchar(20));
INSERT INTO test VALUES (1, 'test1');
INSERT INTO test VALUES (2, 'test2');