#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(n)
*/
void Multime::redim()
{
	TElem* elemsNou = new TElem[2 * cp];
	for (int i = 0; i < n; i++) {
		elemsNou[i] = elems[i];
	}
	cp = cp * 2;
	delete[] elems;
	elems = elemsNou;

}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
Multime::Multime() {
	this->cp = 2;
	this->n = 0;
	elems = new TElem[cp];
}

/*
	COMPLEXITATE
	caz favorabil : vectorul nu trebuie redimensionat -> theta(n)
	caz nefavorabil: elementul exista dar vectorul trebuie redimensionat -> theta(n^2)
	caz mediu: elementul poate fi pe orice pozitie -> theta(n^2)
	===> O(n^2)
*/
bool Multime::adauga(TElem elem) {
	if (cauta(elem) == true)
		return false;
	if (n == cp)
		redim();
	this->elems[n++] = elem;
	return true;
}

/*
	COMPLEXITATE
	caz favorabil : vectorul este vid -> theta(1) 
	caz nefavorabil: elementul este pe ultima pozitie -> theta(n)
	caz mediu: elementul poate fi pe orice pozitie -> theta(n)
	===> O(n)
*/
bool Multime::sterge(TElem elem) {
	int poz = -1;
	for (int i = 0; i < n; i++)
		if (elems[i] == elem) {
			poz = i;
			break;
		}
	
	if (poz == -1) return false;

	while (poz < n - 1) {
		elems[poz] = elems[poz + 1];
		poz++;
	}
	n--;
	return true;
}

/*
	COMPLEXITATE
	caz favorabil : elementul cautat este primul sau vectorul este vid -> theta(1) 
	caz nefavorabil: elementul cautat este ultimul -> theta(n)
	caz mediu: elementul cautat poate fi pe orice pozitie -> theta(n)
	===> O(n)
*/
bool Multime::cauta(TElem elem) const {
	for (int i = 0; i < n; i++)
		if (elems[i] == elem)
			return true;
	return false;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
int Multime::dim() const {
	return n;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
bool Multime::vida() const {
	return n == 0;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(n)
*/
Multime::~Multime() {
	delete[] elems;
}


/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

