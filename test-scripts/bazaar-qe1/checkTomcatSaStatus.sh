#!/bin/sh
#kill tomcat pid  restart tomcat
#Author jun.cui@hpe.com
#check tomcat server status for bazaar
pidlist=`ps -ef|grep apache-tomcat-bazaar|grep -v "grep"|awk '{print $2}'`
echo "the tomcat pid process is ->" $pidlist
if [ "$pidlist" = "" ]
   then
       echo "no tomcat pid alive!"
       sh /opt/apache-tomcat-bazaar/bin/startup.sh &
else
  echo "tomcat service starting now"
fi
sleep 5

#check sa status for server

sapidlist=`ps -ef|grep bazaar-sa|grep -v "grep"|awk '{print $2}'`
echo "the bazaar-sa pid process is ->" $sapidlist
if [ "$sapidlist" = "" ]
   then
       echo "no bazaar-sa pid alive!"
       sh /opt/golangserver/bin/start.sh &
else
  echo "bazaar-sa service starting now"
fi
sleep 5
#check other common componets for bazaar



echo "bazaar health check service has been completed."















