#include "Colectie.h"
#include "IteratorColectie.h"
using namespace std;

// O(1)
int hashCode(TElem e) {
	return abs(e);
}

// O(1)
int Colectie::dispersie(TElem e) const {
	return hashCode(e) % m;
}

// THETA(N)
void Colectie::actPrimLiber() {
	primLiber++;
	while (primLiber < m and e[primLiber] != NIL)
		primLiber++;
}

// THETA(N)
Colectie::Colectie() {
	m = CAPACITATE;
	e = new TElem[m];
	urm = new int[m];
	nrElems = 0;

	// initializam vectorii
	for (int i = 0; i < m; i++) {
		e[i] = NIL;
		urm[i] = NIL;
	}

	primLiber = 0; // initializare de la pozitia 0
}

// THETA(N)
void Colectie::adauga(TElem elem) {

	int poz = dispersie(elem);
	if (e[poz] == NIL) // pozitia este libera
	{
		e[poz] = elem; // adaugam elementul
		nrElems++;
		if (poz == primLiber) // actualizam primLiber
			actPrimLiber();
		return;
	}

	//	 pozitia precendeta lui poz, pentru a reface inlantuirea 
	//	 daca pozitia nu este libera
	int pre_poz = NIL;

	while (poz != NIL) // iteram pana gasim capatul inlantuirii
	{
		pre_poz = poz;
		poz = urm[poz];
	}

	if (primLiber >= m) {
		throw std::exception();
	}

	e[primLiber] = elem;
	urm[pre_poz] = primLiber;
	nrElems++;
	actPrimLiber();


}

// O(N)
bool Colectie::sterge(TElem elem) {
	int i = dispersie(elem);
	int j = NIL;
	int k = 0;
	while (j == NIL && k < m) {
		if (urm[k] == i)
			j = k;
		else
			k++;
	}

	while (i != NIL) {
		if (e[i] == elem)
			break;
		j = i; 
		i = urm[i];
	}

	if (i == NIL) 
		return false;
	else
	{
		bool gata = false;
		do {
			int pa = i;
			int p = urm[i];
			while (p != NIL && dispersie(e[p]) != i) {
				pa = p;
				p = urm[p];
			}
			if (p == NIL)
				gata = true;
			else {
				e[i] = e[p];
				i = p;
				j = pa;
			}

		} while (gata == false);

		if (j != NIL) urm[j] = urm[i];
		e[i] = NIL;
		urm[i] = NIL;
		if (primLiber > i)primLiber = i;
		nrElems--;
		return true;
	}

}

// THETA(N)
bool Colectie::cauta(TElem elem) const {
	int poz = dispersie(elem);
	if (e[poz] == NIL) return false;
	
	while (urm[poz] != NIL) {
		if (e[poz] == elem)
			return true;
		poz = urm[poz];
	}

	if (e[poz] == elem) return true;
	
	return false;
}

// THETA(N)
int Colectie::nrAparitii(TElem elem) const {
	int poz = dispersie(elem);
	if (e[poz] == NIL) return 0;

	int nrAparitii = 0;
	while (urm[poz] != NIL) {
		if (e[poz] == elem)
			nrAparitii++;
		poz = urm[poz];
	}

	if (e[poz] == elem) nrAparitii++;
	return nrAparitii;
}

// O(1)
int Colectie::dim() const {
	return nrElems;
}

// O(1)
bool Colectie::vida() const {
	return dim() == 0;
}

// O(1)
IteratorColectie Colectie::iterator() const {
	return  IteratorColectie(*this);
}

// O(1)
Colectie::~Colectie() {
	delete[] e;
	delete[] urm;
}


/*
	Complexitate: theta(n^2)

	Pre: a: colectia curenta  ,  b: colectia cu care se intersecteaza
	Post: a' = a int b

	SUBALGORITM intersectie(a, b)
	|	ib <- b.iterator();	
	|	CAT TIMP ib.valid() EXECUTA
	|	|
	|	|	nrA <- a.nrAparitii(ib.element())
	|	|	nrB <- b.nrAparitii(ib.element())
	|	|	
	|	|	DACA nrA != 0 SI nrA > nrB ATUNCI
	|	|	|	CAT TIMP nrA > nrB EXECUTA
	|	|	|	|	a.sterge(ib.element())
	|	|	|	|	nrA <- nrA - 1
	|	|	|	SF_CAT_TIMP
	|	|	SF_DACA
	|	|
	|	|	ib.urmator()
	|	|
	|	SF_CAT_TIMP
	|
	|	ia <- a.iterator()
	|	CAT TIMP ia.valid() EXECUTA
	|	|	DACA b.cauta(ia.element()) = false ATUNCI
	|	|	|	
	|	|	|	a.sterge(ia.element());
	|	|	|
	|	|	SF_DACA
	|	SF_CAT_TIMP
	|
	SF_SUBALGORITM
*/
void Colectie::intersectie(const Colectie& b)
{
	IteratorColectie ib = b.iterator();
	while (ib.valid())
	{
		int nrA = nrAparitii(ib.element());
		int nrB = b.nrAparitii(ib.element());
		
		if (nrA != 0 && nrA > nrB) {
				while (nrA > nrB) {
					sterge(ib.element());
					nrA--;
				}
		}
		ib.urmator();
	}

	IteratorColectie ia = iterator();
	ia.prim();
	while (ia.valid())
	{
		if (b.cauta(ia.element()) == false)
			sterge(ia.element());
		ia.urmator();
	}


}


