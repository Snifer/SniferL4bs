#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# maillove.py
#Realizado por Jose Moruno Cadima a.k.a Snifer
# URL: http://www.sniferl4bs.com/2014/07/automatizacion-reconquistando-la-novia.html
# www.sniferl4bs.com

import mimetypes
import os
import smtplib
import sys

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# export MAIL_FROM='mail_from@mail.com'
# export MAIL_PASS='password mail'
# export MAIL_TO='mail_to@mail.com'
mail_from = os.environ.get('MAIL_FROM')
mail_pass = os.environ.get('MAIL_PASS')
mail_to = os.environ.get('MAIL_TO')
fortune_file = 'computers'
cowsay_img = 'kiss'

if True == os.path.exists('/tmp/mail_log.txt'):
    os.remove('/tmp/mail_log.txt')

os.system("fortune %s | cowsay -f %s | tee /tmp/mail_log.txt" % (fortune_file, cowsay_img))

attach_file = MIMEBase('multipart', 'encrypted')
with open('/tmp/mail_log.txt', 'rb') as file:  #Direccion del Archivo
    attach_file.set_payload(file.read())
    attach_file.add_header('Content-Disposition', 'attachment', filename='Una Frase al Día.txt')

msg = MIMEMultipart()
msg['From'] = (mail_from)
msg['To'] = (mail_to)
msg['Subject'] = 'Una frase al dia'
msg.attach(attach_file)

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(mail_from, mail_pass)
mailServer.sendmail(mail_from, mail_to, msg.as_string())
mailServer.close()