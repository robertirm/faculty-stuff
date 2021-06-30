#include "IteratorMDO.h"
#include "MDO.h"
#include <iostream>
#include <vector>

#include <exception>
using namespace std;



// theta(n)
void MDO::redim()
{
	Nod* elemsNou = new Nod[2 * cp];
	int* urmNou = new int[2 * cp];

	for (int i = 0; i < n; i++) {
		elemsNou[i] = elems[i];
		urmNou[i] = urm[i];
	}
	for (int i = n; i < 2 * cp - 1; i++)
		urmNou[i] = i + 1;
	urmNou[2 * cp - 1] = -1;
	cp = cp * 2;
	delete[] elems;
	delete[] urm;
	elems = elemsNou;
	urm = urmNou;
}



// theta(n)
MDO::MDO(Relatie r) {
	this->rel = r;
	this->nrElems = 0;
	this->cp = 2;
	this->n = 0;
	elems = new Nod[cp];
	urm = new int[cp];

	prim = -1;
	for (int i = 0; i < cp - 1; i++)
		urm[i] = i + 1;
	urm[cp - 1] = -1;
	primLiber = 0;
}

// theta(n)
void MDO::adauga(TCheie c, TValoare v) {

	//cout << "PRIM: " << prim << " PRIMLIBER: " << primLiber << endl;

	nrElems++;

	// daca cheia exista se adauga doar valoarea
	int i = prim;
	while (i != -1) {
		if (elems[i].cheie == c) {
			elems[i].adauga(v);
			return;
		}
		i = urm[i];
	}
	
	// adaugam noua cheie
	if (n == cp-1)redim();
	Nod nod;
	i = creeazaNod(nod);
	urm[i] = prim;
	prim = i;
	elems[prim].cheie = c;
	elems[prim].adauga(v);
	n++;


	// daca e prima cheie putem iesi
	if (nrElems == 1)return;

	// daca este ok sa fie la inceput putem iesi
	if (rel(elems[prim].cheie, elems[urm[prim]].cheie))return;

	// daca mai sunt chei, noua cheie trebuie inserata a.i. ordinea sa se pastreze
	int viitor_prim = prim[urm];
	int j = prim;
	i = prim[urm];
	while (i != -1) {
		if (rel(elems[prim].cheie, elems[i].cheie)) {
			urm[prim] = urm[j];
			urm[j] = prim;
			break;
		}
		i = urm[i];
		j = urm[j];
	}
	if (i == -1) {
		urm[prim] = urm[j];
		urm[j] = prim;

	}

	prim = viitor_prim;

}


// theta(n)
vector<TValoare> MDO::cauta(TCheie c) const {
	int i = prim;
	while (i != -1) {
		if (elems[i].cheie == c) {
			return elems[i].toateValorile();
		}
		i = urm[i];
	}
	return vector<TValoare>  ();
}


// theta(n^2)
bool MDO::sterge(TCheie c, TValoare v) {
	int i = prim;
	while (i != -1) {
		if (elems[i].cheie == c) {
			if (elems[i].stergere(v))
			{
				nrElems--;
				return true;
			}
			else return false;
		}
		i = urm[i];
	}
	return false;
}

// O(1)
int MDO::dim() const {
	return nrElems;
}

// O(1)
bool MDO::vid() const {
	return nrElems == 0;
}

// O(1)
IteratorMDO MDO::iterator() const {
	return IteratorMDO(*this);
}

// theta(n)
MDO::~MDO() {
	int i = prim;
	while (i != -1) {
		elems[i].~Nod();
		i = urm[i];
	}
	delete[] urm;
	delete[] elems;
}




/*

	COMPLEXITATE : theta(mdoCurent.dim * mdOther.dim) care apartine la O(n^2)


	Pre: mdoCurent: MDO , mdoOther: MDO
	Post: in mdoCurent se vor adauga elementele din mdoOther care nu apar in mdoCurent 
		si se va returna numarul de astfel de elemente

	SUBALGORIM adaugaInexistente(mdoCurent, mdoOther)
	|	nrAdaugari <- 0;
	|	itCurent <- mdoCurent.iterator()
	|	
	|	|CAT TIMP itCurent.valid EXECUTA
	|	|	nuExista <- true
	|	|	eCurent <- itCurent.element()
	|	|	itOther <- mdoOther.iterator()
	|	|	
	|	|	CAT TIMP itOther.valid EXECUTA
	|	|	|	eOther <- itOther.element()
	|	|	|	DACA eCurent == eOther ATUNCI
	|	|	|	|	nuExista <- false
	|	|	|	|	break cat timp
	|	|	|	SF_DACA
	|	|	|
	|	|	|	Other <- itOther.urmator()
	|	|	SF_CAT_TIMP
	|	|
	|	|	DACA nuExista == true ATUNCI
	|	|	|	mdoCurent.adauga(eCurent.cheie, eCurent.valoara)
	|	|	|	nrAdaugari <- nrAdaugari + 1
	|	|	SF_DACA
	|	|
	|	|	itCurent <- itCurent.urmator()
	|	SF_CAT_TIMP
	|
	|	RETURNEAZA nrAdaugari
	SF_SUBALGORITM


*/
int MDO::adaugaInexistente(MDO& mdo)
{
	int nrAdaugari = 0;
	IteratorMDO itCurent = iterator();
	while (itCurent.valid()) {
		bool nuExista = true;
		TElem eCurent = itCurent.element();
		IteratorMDO itOther = mdo.iterator();
		while (itOther.valid()) {
			TElem eOther = itOther.element();
			if (eCurent == eOther) {
				nuExista = false;
				break;
			}
			itOther.urmator();
		}

		if (nuExista) {
			adauga(eCurent.first, eCurent.second);
			nrAdaugari++;
		}
		itCurent.urmator();
	}
	return nrAdaugari;

}



// theta(n)
void Nod::redim()
{
	TValoare* elemsNou = new TValoare[2 * cp];
	int* urmNou = new int[2 * cp];


	for (int i = 0; i < n; i++) {
		elemsNou[i] = elems[i];
		urmNou[i] = urm[i];
	}
	for (int i = n; i < 2*cp - 1; i++)
		urmNou[i] = i + 1;
	urmNou[2 * cp - 1] = -1;
	cp = cp * 2;
	delete[] elems;
	delete[] urm;
	elems = elemsNou;
	urm = urmNou;
}

// theta(n)
Nod::Nod()
{
	this->cp = 2;
	this->n = 0;
	elems = new TValoare[cp];
	urm = new int[cp];

	prim = -1;
	for (int i = 0; i < cp - 1; i++)
		urm[i] = i + 1;
	urm[cp-1] = -1;
	primLiber = 0;
}

// theta(1)
void Nod::adauga(TValoare v)
{
	if (cp-1 == n)redim();
	int i = creeazaNod(v);
	urm[i] = prim;
	prim = i;
	n++;

}

// theta(n)
bool Nod::stergere(TValoare v)
{
	if (elems[prim] == v) {
		int i = prim;
		prim = urm[prim];
		n--;
		dealoca(i);
		return true;
	}
	int i = prim;
	while (urm[i] != -1) {
		if (elems[urm[i]] == v) {
			urm[i] = urm[urm[i]];
			dealoca(urm[i]);
			n--;
			return true;
		}
		i = urm[i];
	}
	return false;
}

// theta(n)
vector<TValoare> Nod::toateValorile()
{
	vector<TValoare> v;
	int i = prim;
	while (i != -1) {
		TValoare val = elems[i];
		v.push_back(val);
		i = urm[i];
	}
	return v;
}

// O(1)
IteratorNod Nod::iterator() const
{
	return IteratorNod(*this);
}


