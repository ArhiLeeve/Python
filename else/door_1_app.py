#!/usr/bin/python

from gpiozero import Button
import time
import datetime
import smtplib
import logging

logging.basicConfig(filename='/home/talo/python/door_1.log',level=logging.DEBUG)
button = Button(18)

while True:
    button.wait_for_press()
    with open("/home/talo/python/door_1_mailstate.txt",'r') as door_1_mailstate:
        tf = door_1_mailstate.read()
        #print("Etuovi Auki   " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 1 ") + ("Mailsend: " + tf))
        logging.debug("Etuovi Auki   " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 1 ") + ("Mailsend: " + tf))
        fp = open('/home/talo/python/door_1_data.txt', 'w')
        fp.write('1')
        #print("Asennossa: 1 ")
        fp.close()
    with open("/home/talo/python/door_1_mailstate.txt",'r') as door_1_mailstate:
        tf = door_1_mailstate.read()
    #print("     mail: " + tf)
    if tf == "0":
        server = smtplib.SMTP('smtp.mail.com', 587)
        server.starttls()
        server.login("U_S_E_R@mail.com", "P_A_S_S_W_O_R_D")
        msg = "sst63 Etuovi auki !"
        server.sendmail("U_S_E_R@mail.com", "U_S_E_R@mail.com", msg)
        server.sendmail("U_S_E_R@mail.com", "U_S_E_R@mail.com", msg)
        server.quit()
        logging.debug('Mail sended')
        d1m = open("/home/talo/python/door_1_mailstate.txt",'w')
        d1m.write('1')
        d1m.close()
        logging.debug('Mailstate asetettu = 1')
        #print(tf)

    button.wait_for_release()
    with open("/home/talo/python/door_1_mailstate.txt",'r') as door_1_mailstate:
        tf = door_1_mailstate.read()
        #print("Etuovi Kiinni " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 0 ") + ("Mailsend: " + tf))
        logging.debug("Etuovi Kiinni " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 0 ") + ("Mailsend: " + tf))
        #print(' Timestamp: {:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now()) + ('0'))
        fr = open('/home/talo/python/door_1_data.txt', 'w')
        fr.write('0')
        #print("  Asennossa: 0 ")
        fr.close()
 
#else:
#  fp.close()
#  fr.close()
 
