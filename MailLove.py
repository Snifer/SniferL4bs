#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# maillove.py
#Realizado por Jose Moruno Cadima a.k.a Snifer
# URL: http://www.sniferl4bs.com/2014/07/automatizacion-reconquistando-la-novia.html
# www.sniferl4bs.com

import argparse
import os
import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

parser = argparse.ArgumentParser(description='Send a mail generated with cowsay and fortune')
parser.add_argument('-f', '--fortune', default='computers', help='Name of the fortune file (default: %(default)s)')
parser.add_argument('-c', '--cowfile', default='koala', help='Name of the cowsay file (default: %(default)s)')
parser.add_argument('-s', '--sender', help='The value of the From: header')
parser.add_argument('-r', '--recipient', help='The value of the To: header')
parser.add_argument('-p', '--password', help='Email password')

args = parser.parse_args()

print args

mail_from = args.sender
mail_pass = args.password
mail_to = args.recipient
fortune_file = args.fortune
cowsay_img = args.cowfile

if None == mail_from:
    # export MAIL_FROM='mail_from@mail.com'
    mail_from = os.environ.get('MAIL_FROM')
    if None == mail_from:
        raise Exception('Error: mail From')

if None == mail_pass:
    # export MAIL_PASS='password mail'
    mail_pass = os.environ.get('MAIL_PASS')
    if None == mail_pass:
        raise Exception('Error: mail Password')

if None == mail_to:
    # export MAIL_TO='mail_to@mail.com'
    mail_to = os.environ.get('MAIL_TO')
    if None == mail_to:
        raise Exception('Error: mail To')

if True == os.path.exists('/tmp/mail_log.txt'):
    os.remove('/tmp/mail_log.txt')

os.system("fortune %s | cowsay -f %s | tee /tmp/mail_log.txt" % (fortune_file, cowsay_img))

attach_file = MIMEBase('multipart', 'encrypted')
with open('/tmp/mail_log.txt', 'rb') as file:  #Direccion del Archivo
    attach_file.set_payload(file.read())
    attach_file.add_header('Content-Disposition', 'attachment', filename='Una Frase al Dia.txt')

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
