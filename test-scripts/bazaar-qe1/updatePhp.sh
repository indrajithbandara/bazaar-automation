#!/bin/bash

cd /var/www/html/bazaar-web
ls -adl .env|sed -i 's/bazaar-comp-image/10.33.206.10/g' .env
ls -adl .env|sed -i 's/10\.33\.205\.10/10.33.206.10/g' .env
echo "update bazaar-web .env file has been completed."

cd /var/www/html/bazaar-web-management/ 
ls -adl .env|sed -i 's/bazaar-comp-image/10.33.206.10/g' .env
echo "update bazaar-web-management .env file has been completed."
