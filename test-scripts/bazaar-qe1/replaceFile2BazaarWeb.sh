#!/bin/sh
#kill tomcat pid  restart tomcat
#Author jun.cui@hpe.com 

#cd /var/www/html
#ls -ll
#chmod 777 bazaarwebworkspace.tar.gz
#tar xvzf bazaarwebworkspace.tar.gz
#sleep 2

#mv bazaar-web-qe bazaar-web
#chmod -R 777 bazaar-web
#chown -R labuser:labuser bazaar-web

cd bazaar-web
composer dump-autoload
sleep 2

sed -i 's/bazaar-comp-image/10.33.206.10/g' config/constant.php
ls -adl .env|sed -i 's/bazaar-comp-image/10.33.206.10/g' .env
ls -adl .env|sed -i 's/APP_TEST=false/APP_TEST=true/g' .env
ls -adl .env|sed -i 's/COMPONENT_PUBLIC_IP=false/COMPONENT_PUBLIC_IP=true/g' .env
ls -adl .env|sed -i 's/img\.hpebazaar\.tk/10.33.206.10/g' .env
ls -adl .env|sed -i 's/www\.hpebazaar\.tk/10.33.206.10/g' .env

httpd -k  restart
sleep 2
netstat -ntlp|grep 80

