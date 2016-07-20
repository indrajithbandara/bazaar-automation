#!/bin/sh
#kill tomcat pid  restart tomcat
#Author jun.cui@hpe.com 
#cd /var/www/html
#ls -ll bazaar_admin_workspace.tar.gz
#tar xvzf bazaar_admin_workspace.tar.gz
#ls -ll bazaar-webadmin-qe
#mv bazaar-webadmin-qe bazaar-web-management
#chown -R labuser:labuser bazaar-web
#chmod -R 777 bazaar-web-management

cd bazaar-web-management
composer dump-autoload
sleep 3

sed -i 's/bazaar-comp-image/10.33.206.13/g' config/constant.php
ls -adl .env|sed -i 's/bazaar-comp-image/10.33.206.13/g' .env
ls -adl .env|sed -i 's/APP_TEST=false/APP_TEST=true/g' .env
ls -adl .env|sed -i 's/COMPONENT_PUBLIC_IP=false/COMPONENT_PUBLIC_IP=true/g' .env
ls -adl .env|sed -i 's/img\.hpebazaar\.tk/10.33.206.13/g' .env
ls -adl .env|sed -i 's/www\.hpebazaar\.tk/10.33.206.13/g' .env

httpd -k restart
sleep 2
netstat -ntlp|grep 80

