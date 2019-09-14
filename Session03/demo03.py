age = 20

if age >= 21:
    print('yes, you can')
else:
    print('Sorry, you can\'t.')

#3.0 - 

import time
time.time()
1437746094.5735958

Days=time.time()//(60*60*24)
Hours=(time.time()%(60*60*24))//(60*60)
Minutes=(time.time()%(60*60*24))%(60*60)//60
Seconds=(time.time()%(60*60*24))%(60*60)%60

print("The time is %d: %d: %d: %d" %(Days, Hours, Minutes, Seconds")