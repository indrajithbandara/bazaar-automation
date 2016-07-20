http://www.ibm.com/developerworks/cn/linux/l-lpic1-105-3/

http://blog.itpub.net/28883355/viewspace-1125122/

配置第一个iSCSI设备  #在/opt/下生成64G大的空洞设备文件  #请将opt修改为实际的目录，并根据实际情况设置设备文件大小  
#生成空洞文件速度很快的，且在真正使用之前不占用磁盘实际空间  
dd if=/dev/zero of=/opt/iscsi.[配置文件中Target的名称].img bs=1G count=64 seek=64     
#cout是从什么开始，一般设置为0  
#生成256G的例子  
dd if=/dev/zero of=/opt/iscsi/iqn.2009-04.com.haoyuan-inc:storage.disk.oracle.01.img bs=1G count=0 seek=256    
 vim /etc/ietd.conf  
#编辑Target名称，
例如：iqn.2009-04.com.haoyuan-inc:storage.disk.share.01  #编辑LUN段内容，
例如：Lun 0 Path=/opt/iscsi.iqn.2009-04.com.haoyuan-inc:storage.disk.share.01.image,Type=fileio  
#不要设置XXXUser，允许任何人访问     
#重启iscsi-target  