#Script Realizado por @ericBalderrama

echo -e "Script para seguir usando kali 1.1.a pero con los repos del Kali Sana \n"

#Borramos remos viejos
rm -Rf /etc/apt/source.list

echo > #deb http://http.kali.org/kali kali main non-free contrib
echo >> #deb-src http://http.kali.org/kali kali main non-free contrib

echo >> ## Security updates
echo >> #deb http://security.kali.org/kali-security kali/updates main contrib non-free

echo >> #Kali Sana
echo >> deb http://http.kali.org/kali sana main non-free contrib
echo >> deb http://security.kali.org./kali-security sana/updates main contrib non-free

echo >> #Source repos
echo >> deb-src http://http.kali.org/kali sana main non-free contrib
echo >> deb-src http://security.kaly.org/kali-security sana/updates main contrib non-free


#Limpiamos apt
sudo apt-get clean

#Updateamos repos
sudo apt-get update

#Upgradeamos todas las aps
sudo apt-get upgrade

#Upgradeamos la distro
sudo apt-get dist-upgrade

echo "Listo!"
