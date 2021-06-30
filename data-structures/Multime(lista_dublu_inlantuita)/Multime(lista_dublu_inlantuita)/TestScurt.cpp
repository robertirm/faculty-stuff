#include "TestScurt.h"
#include <assert.h>
#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>
void testAll() { //apelam fiecare functie sa vedem daca exista
	Multime m;
	assert(m.vida() == true);
	assert(m.dim() == 0); //adaug niste elemente
	assert(m.adauga(5)==true);
	assert(m.adauga(1)==true);
	assert(m.adauga(10)==true);
	assert(m.adauga(7)==true);
	assert(m.adauga(1)==false);
	assert(m.adauga(10)==false);
	assert(m.adauga(-3)==true);
	assert(m.dim() == 5);
	assert(m.cauta(10) == true);
	assert(m.cauta(16) == false);
	assert(m.sterge(1) == true);
	assert(m.sterge(6) == false);
	assert(m.dim() == 4);


	IteratorMultime im = m.iterator();
	im.prim();
	int s = 0;
	while (im.valid()) {
		TElem e = im.element();
		s += e;
		im.urmator();
	}
	assert(s == 19);



	///
	Multime m2;
	m2.adauga(1);
	m2.adauga(2);
	m2.adauga(3);
	m2.adauga(4);
	m2.adauga(5);

	IteratorMultime it2 = m2.iterator();
	it2.prim(); 
	it2.urmator(); 
	it2.urmator(); 
	assert(it2.element() == 3);
	it2.anterior();
	assert(it2.element() == 4);
	it2.anterior();
	assert(it2.element() == 5);
	it2.anterior();
	assert(it2.valid() == false);
}
