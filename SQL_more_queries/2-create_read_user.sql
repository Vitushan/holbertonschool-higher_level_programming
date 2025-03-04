-- print privileges for user_0d_1
-- print privileges for user_0d_2
IF user_0d_2 EXISTS
IF hbtn_0d_2 EXISTS
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS INSERT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
