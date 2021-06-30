#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>

Multime::Multime() {
	primul = nullptr;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz nefavorabil = theta(n)
*/
bool Multime::adauga(TElem elem) {
	// adaugare la inceput
	if (cauta(elem) == true)
		return false;

	Pnod nouNod = new Nod(elem, nullptr, primul);

	if (primul != nullptr) {
		primul->ant = nouNod;
		
	}
	primul = nouNod;
	return true;
}

/*
	COMPLEXITATE
	caz favorabil: elementul este pe prima pozitie din lista -> theta(1)
	caz nefavorabil: elementul nu exista in lista -> theta(n)
	caz mediu: elementul poate fi pe orice pozitie -> theta(n)
	---> O(n)
*/
bool Multime::sterge(TElem elem) {
	Pnod p = primul;
	if (primul == nullptr) return false;
	if (primul->info == elem) {
		if (primul->urm == nullptr)
		{
			p = primul;
			primul = nullptr;
			delete p;
			return true;
		}
		primul->urm->ant = nullptr;
		Pnod nou_primul = primul->urm;
		delete p;
		primul = nou_primul;
		return true;
	}
	while (p->urm != nullptr) {
		if (p->info == elem) {
			p->ant->urm = p->urm;
			p->urm->ant = p->ant;
			delete p;
			return true;
		}
		p = p->urm;
	}
	if (p->info == elem) {
		p->ant->urm = nullptr;
		delete p;
		return true;
	}
	return false;
	
}

/*
	COMPLEXITATE
	caz favorabil: elementul este pe prima pozitie din lista -> theta(1)
	caz nefavorabil: elementul nu exista in lista -> theta(n)
	caz mediu: elementul poate fi pe orice pozitie -> theta(n)
	---> O(n)
*/
bool Multime::cauta(TElem elem) const {
	Pnod p = primul;
	while (p != nullptr) {
		if (p->info == elem)
			return true;
		p = p->urm;
	}
	return false;
}

/*
	COMPLEXITATE
	---> O(n)
*/
int Multime::dim() const {
	Pnod p = primul;
	int s = 0;
	for (; p != NULL; s++) {
		p = p->urm;
	}
	return s;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz nefavorabil = theta(1)
*/
bool Multime::vida() const {
	return primul == nullptr;
}

/*
	COMPLEXITATE
	---> O(n)
*/
Multime::~Multime() {
	while (primul != nullptr) {
		Pnod p = primul;
		primul = primul->urm;
		delete p;
	}
}


/*
	COMPLEXITATE
	---> O(1)
*/
IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

