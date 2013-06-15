#!/usr/bin/env python

def cetak(arg):
	print arg;

def tambah(arg1, arg2):
	print arg1 + arg2;

def kurang(arg1, arg2):
	print arg1 - arg2;

def getAngkaKuadrat(arg):
	return arg **2;
def angkaDiKaliDua(arg):
	return arg *2;

tambah(3,7);
kurang(10,5);
angkaGue = getAngkaKuadrat(angkaDiKaliDua(2));
cetak(angkaGue);