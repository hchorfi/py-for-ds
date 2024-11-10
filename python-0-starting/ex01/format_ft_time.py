# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
import time as time
seconds_since_epoch = time.time()
date_struct = time.localtime(seconds_since_epoch)

print (f'Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation')
print (f'{time.strftime("%b %d %Y", date_struct)}')
