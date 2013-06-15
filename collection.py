#!/usr/bin/env python


asbak = ["abu", "puntung", "kwuaci", 3.14,1];
print asbak;
for i in xrange(0, len(asbak)):
	print asbak[i];
beberapaAngka = [11, 3, 7, 9, 10];
print beberapaAngka;
#tambahin 10 ke dalam array beberapaAngka
beberapaAngka.append(10);

def sumArray(array):
	a = int(0);
	if type(array[0]) != int:
		return "the element is not a number";
	else:
		a = array[0];
		for x in xrange(1, len(array)):
			if type(array[x]) != int:
				return "the element is not a number";
			else:
				a = a + array[x];
		return a;
print sumArray(beberapaAngka);

	