#!/usr/bin/python

from gpiozero import Button
import time
import datetime
import smtplib
import logging

logging.basicConfig(filename='/home/talo/python/door_2.log',level=logging.DEBUG)
button = Button(23)

while True:
 button.wait_for_press()
 
 with open("/home/talo/python/door_2_mailstate.txt",'r') as door_2_mailstate:
  tf = door_2_mailstate.read()	
 #print("Takaovi Kiinni " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 0 ") + ("Mailsend: " + tf))
 logging.debug("Takaovi Kiinni " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 0 ") + ("Mailsend: " + tf))
 fp = open('/home/talo/python/door_2_data.txt', 'w')
 fp.write('0')
 #print("Asennossa: 0 ")
 fp.close()

	
 button.wait_for_release()
 
 with open("/home/talo/python/door_2_mailstate.txt",'r') as door_2_mailstate:
  tf = door_2_mailstate.read()
 #print("Takaovi Auki   " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 1 ") + ("Mailsend: " + tf))
 logging.debug("Takaovi Auki   " + ('{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())) + (" Tila: 1 ") + ("Mailsend: " + tf))
 #print(' Timestamp: {:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now()) + ('1'))
 fr = open('/home/talo/python/door_2_data.txt', 'w')
 fr.write('1')
 #print("  Asennossa: 1 ")
 fr.close()
 
 with open("/home/talo/python/door_2_mailstate.txt",'r') as door_2_mailstate:
  tf = door_2_mailstate.read()
  #print("   mail: " + tf)
 if tf == "0":
  server = smtplib.SMTP('smtp.mail.com', 587)
  server.starttls()
  server.login("U_S_E_R@gmail.com", "P_A_S_S_W_O_R_D")
  msg = "sst63 Takaovi auki !"
  server.sendmail("U_S_E_R@mail.com", "U_S_E_R@mail.com", msg)
  server.sendmail("U_S_E_R@mail.com", "U_S_E_R@mail.com", msg)
  server.quit()
  logging.debug('Mail sended')

  d1m = open("/home/talo/python/door_2_mailstate.txt",'w')
  d1m.write('1')
  d1m.close()
  logging.debug('Mailstate asetettu = 1')
  #print(tf)
 else:
  fp.close()
  fr.close()
