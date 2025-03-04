-- Creates the MySQL server user user_0d_1
-- if the user already exists, this script should not fail
IF user_0d_1 EXISTS CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'
