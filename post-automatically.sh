#!/bin/bash
# 
#File Name: post-automatically
#Realizado por RizelTane a.k.a Rizel twitter:@RizelTane
# URL English Version: http://www.sniferl4bs.com/2014/07/automation-posting-phrase-on-twitter.html
#     Spanish Version:  http://www.sniferl4bs.com/2014/07/automatizacion-posteando-una-frase-en.html
# www.sniferl4bs.com

echo "This is the text that will be posted: $1"
#$( echo VAR=value )
file='temporary.txt'
eval echo `touch $file`
eval echo `echo $1>>$file`
#now="$(date +'%d/%m/%Y')"
#whoami
csv=`t whoami -c`
 
#grep -o . <<< $csv | while read letter;  do echo "my letter is $letter" ; done
#echo $csv
 
for (( i=0, c=0; i<${#csv}; i++ )); do
  if [[ ${csv:$i:1} == "," ]]
  then
 let c++
 if [ $c == 23 ]
 then
   #while
   #echo ${csv:$i:1}
   #echo ${csv:$i:2}
   #echo ${csv:$i:3}
   #echo ${csv:$i:4}
   #echo ${csv:$i:5}
   #echo ${csv:$i:6}
   #echo ${csv:$i:7}
   #echo ${csv:$i:9}
   #echo ${csv:$i:10}
   #echo ${csv:$i:11}
   for (( j=1;  ${csv:$i:$j} != ","  ; j++ )); do
    echo ${csv:$i:$j}
   done
 fi
  fi
done
 
 
 
picture=`date +'%F%T'`
image_magick="convert
-background turquoise
-fill white
-pointsize 18
-size 500x500
-gravity center
label:@$file
$picture.gif"
eval $image_magick
 
 
 
echo "Done boss."