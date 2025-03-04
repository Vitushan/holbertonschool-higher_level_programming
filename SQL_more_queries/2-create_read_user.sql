-- Creates the databases
-- create user_0d_2
CREATE DATABASES IF NOT EXISTS
'hbtn_0d_2';
CREATE USER IF NOT EXISTS
'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO
'user_0d_2'@'localhost';
