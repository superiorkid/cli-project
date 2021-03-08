"""
	membuat program yang menerima masukan panjang password dari user,
	kemudian akan meng-generate random password berdasarkan panjang yang diinputkan
"""

import random
import string

def pw_generate(length):
	_str = string.ascii_letters + string.digits
	return "".join(random.sample(_str, length))

passlen = int(input('masukkan panjang password: '))
print(pw_generate(passlen))


