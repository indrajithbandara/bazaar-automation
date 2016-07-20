#!/bin/bash
#kill tomcat pid  restart tomcat
#Author jun.cui@hpe.com
ps -elf|grep tomcat
pidlist=`ps -ef|grep apache-tomcat-bazaar|grep -v "grep"|awk '{print $2}'`
if [ "$pidlist" = "" ]
   then
       echo "no tomcat pid alive!"
else
  echo "tomcat Id list :$pidlist"
  kill -9 $pidlist
  echo "KILL $pidlist:"
  echo "service stop success"
fi
echo "start tomcat"
cd /opt/apache-tomcat-bazaar/webapps
rm -rf bazaar*.war
rm -rf bazaar*
ls -lat
ps -elf|grep tomcat
chown -R labuser:labuser /opt/opt/javabuilds/bazaar*.war

mv /opt/opt/javabuilds/bazaar*.war /opt/apache-tomcat-bazaar/webapps/
#cd /opt/apache-tomcat-bazaar/bin
#sudo sh /opt/apache-tomcat-bazaar/bin/startup.sh &
#sleep 60
#sh /opt/apache-tomcat-bazaar/bin/startup.sh &
#sleep 30
#ps -elf|grep tomcat

