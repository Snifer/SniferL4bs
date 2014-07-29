#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#maillove.py
#Realizado por Jose Moruno Cadima a.k.a Snifer
# URL: http://www.sniferl4bs.com/2014/07/automatizacion-reconquistando-la-novia.html
# www.sniferl4bs.com
 
import smtplib
import mimetypes
import os
import sys
 
from email.MIMEMultipart import MIMEMultipart
from email.Encoders import encode_base64
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
gmail_to = 'xxxx@gmail.com' #Correo a enviar
gmail_from = 'xxxxxx@gmail.com' #Correo de donde se envia
password='*******' #Contraseña
 
os.system("rm /tmp/log")
#os.system("acpi -i | tee /tmp/log.txt")<
os.system("fortune rizel | cowsay -f kiss | tee /tmp/log")
 
 
msg = MIMEMultipart()
msg['From']= (gmail_from)
msg['To']= (gmail_to)
msg['Subject']="Subject"
 
 
file = open("/tmp/log.txt", "rb") #Direccion del Archivo
attach_file = MIMEBase('multipart', 'encrypted')
attach_file.set_payload(file.read())
file.close()
 
attach_file.add_header('Content-Disposition', 'attachment', filename='Una Frase al Día.txt')#NOMBRE DEL ARCHIVO A ENVIAR QUE SE VERA
msg.attach(attach_file)
 
 
mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_from, password)
mailServer.sendmail(gmail_from, gmail_to, msg.as_string())
mailServer.close()