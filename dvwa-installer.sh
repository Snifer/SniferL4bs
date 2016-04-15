#/bin/bash
echo -e "\n#######################################"
echo -e "# Damn Vulnerable Web App Installer Script #"
echo -e "#######################################"
echo " Coded By: Travis Phillips"
echo " Website: http://theunl33t.blogspot.com"
echo -e -n "\n[*] Changing directory to /var/www..."
cd /var/www > /dev/null
echo -e "Done!\n"

echo -n "[*] Removing default index.html..."
rm index.html > /dev/null
echo -e "Done!\n"

echo -n "[*] Changing to Temp Directory..."
cd /tmp
echo -e "Done!\n"

echo "[*] Downloading DVWA..."
wget http://dvwa.googlecode.com/files/DVWA-1.0.7.zip
#wget http://voxel.dl.sourceforge.net/project/dvwa/DVWA-1.0.7.zip
echo -e "Done!\n"

echo -n "[*] Unzipping DVWA..."
unzip DVWA-1.0.7.zip > /dev/null
echo -e "Done!\n"

echo -n "[*] Deleting the zip file..."
rm DVWA-1.0.7.zip > /dev/null
echo -e "Done!\n"

echo -n "[*] Copying dvwa to root of Web Directory..."
cp -R dvwa/* /var/www > /dev/null
echo -e "Done!\n"

echo -n "[*] Clearing Temp Directory..."
rm -R dvwa > /dev/null
echo -e "Done!\n"

echo -n "[*] Enabling Remote include in php.ini..."
cp /etc/php5/apache2/php.ini /etc/php5/apache2/php.ini1
sed -e 's/allow_url_include = Off/allow_url_include = On/' /etc/php5/apache2/php.ini1 > /etc/php5/apache2/php.ini
rm /etc/php5/apache2/php.ini1
echo -e "Done!\n"

echo -n "[*] Enabling write permissions to /var/www/hackable/upload..."
chmod 777 /var/www/hackable/uploads/
echo -e "Done!\n"

echo -n "[*] Starting Web Service..."
service apache2 start &> /dev/null
echo -e "Done!\n"

echo -n "[*] Starting MySQL..."
service mysql start &> /dev/null
sleep 11
echo -e "Done!\n"

echo -n "[*] Updating Config File..."
cp /var/www/config/config.inc.php /var/www/config/config.inc.php1
sed -e 's/'\'\''/'\''toor'\''/' /var/www/config/config.inc.php1 > /var/www/config/config.inc.php
rm /var/www/config/config.inc.php1
echo -e "Done!\n"

echo -n "[*] Updating Database..."
wget --post-data "create_db=Create / Reset Database" http://127.0.0.1/setup.php &> /dev/null
mysql -u root --password='toor' -e 'update dvwa.users set avatar = "/hackable/users/gordonb.jpg" where user = "gordonb";'
mysql -u root --password='toor' -e 'update dvwa.users set avatar = "/hackable/users/smithy.jpg" where user = "smithy";'
mysql -u root --password='toor' -e 'update dvwa.users set avatar = "/hackable/users/admin.jpg" where user = "admin";'
mysql -u root --password='toor' -e 'update dvwa.users set avatar = "/hackable/users/pablo.jpg" where user = "pablo";'
mysql -u root --password='toor' -e 'update dvwa.users set avatar = "/hackable/users/1337.jpg" where user = "1337";'
echo -e "Done!\n"

echo -e -n "[*] Starting Firefox to DVWA\nUserName: admin\nPassword: password"
firefox http://127.0.0.1/login.php &> /dev/null &
echo -e "\nDone!\n"
echo -e "[\033[1;32m*\033[1;37m] DVWA Install Finished!\n"