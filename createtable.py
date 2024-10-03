from connectdb import mycursor

create_table = "CREATE TABLE IF NOT EXISTS `animals` (`id` BIGINT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255), `image` VARCHAR(255), `region` VARCHAR(255), `predator` TINYINT(1))"
mycursor.execute(create_table)

mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)