-- converts the database hbtn_0c_0 to UTF8(utfmb4, collate: utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- converts the character set of the table first_table to utf8mb4, collation utf8mb4_unicode_ci
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- converts teh character set and collation of the specified field 'name' of the table first_table
ALTER TABLE hbtn_0c_0.first_table 
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;



