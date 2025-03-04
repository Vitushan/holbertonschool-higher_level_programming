-- Creates the MySQL server user user_0d_1
-- if the user already exists, this script should not fail
CREATE USER IF NOT EXISTS
'user_0d_1'@'localhost' IDENTIFIED BY
'user_0d_1_pwd';

-- comments here
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
