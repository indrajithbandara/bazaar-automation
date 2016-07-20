-- SQL statements for bazaar projects--

drop database bazaar_account;
drop database bazaar_billing;
drop database bazaar_deliverymanager;
drop database bazaar_monitor;
drop database bazaar_order;
drop database bazaar_serviceofferings;
drop database bazaar_subscription;

CREATE DATABASE bazaar_account DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_billing DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_deliverymanager DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_monitor DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_order DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_serviceofferings DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE bazaar_subscription DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

show variables like '%character%';
show variables like 'character_set_%';

--mysql mysqldump
mysqldump -u username -p dbname > dbname.sql    
mysqldump -u username -p -d dbname > dbname.sql    
mysqldump -u username -p dbname tablename > tablename.sql    
mysqldump -u username -p -d dbname tablename > tablename.sql   