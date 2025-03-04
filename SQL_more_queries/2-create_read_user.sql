-- print privileges for user_0d_1
-- print privileges for user_0d_2
IF user_0d_2 EXISTS
FROM hbtn_0d_2;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS SELECT FOR 'user_0d_2'@'localhost';
