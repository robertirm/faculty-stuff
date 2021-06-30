#include "TestScurt.h"
#include <assert.h>
#include "Colectie.h"
#include "IteratorColectie.h"




void testAll() { //apelam fiecare functie sa vedem daca exista
	Colectie c;
	assert(c.vida() == true);
	assert(c.dim() == 0); //adaug niste elemente
	c.adauga(5);
	c.adauga(1);
	c.adauga(10);
	c.adauga(7);
	c.adauga(1);
	c.adauga(11);
	c.adauga(-3);
	assert(c.dim() == 7);
	assert(c.cauta(10) == true);
	assert(c.cauta(16) == false);
	assert(c.nrAparitii(1) == 2);
	assert(c.nrAparitii(7) == 1);
	assert(c.sterge(1) == true);
	assert(c.sterge(6) == false);
	assert(c.dim() == 6);
	assert(c.nrAparitii(1) == 1);
	IteratorColectie ic = c.iterator();
	ic.prim();
	while (ic.valid()) {
		TElem e = ic.element();
		ic.urmator();
	}



	/// TEST INTERSECTIE

	Colectie a; 
	a.adauga(1);
	a.adauga(3);
	a.adauga(3);
	a.adauga(3);
	a.adauga(5);

	Colectie b;
	b.adauga(2);
	b.adauga(3);
	b.adauga(3);
	b.adauga(5);
	b.adauga(5);

	// a: 1 3 3 3 5
	// b: 2 3 3 5 5
	// rez-> a: 3 3 5 

	a.intersectie(b);

	assert(a.nrAparitii(1) == 0);
	assert(a.nrAparitii(2) == 0);
	assert(a.nrAparitii(3) == 2);
	assert(a.nrAparitii(5) == 1);
	



}