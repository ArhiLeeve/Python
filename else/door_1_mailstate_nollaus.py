import datetime
d2m = open("/home/talo/python/door_1_mailstate.txt",'w')
d2m.write('0')
d2m.close()
print(("Door1_Mailstate Tilassa: 0 ") + (' {:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())))

