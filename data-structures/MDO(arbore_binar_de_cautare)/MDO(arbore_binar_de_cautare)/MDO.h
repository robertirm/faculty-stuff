#pragma once

#include <vector>
#include <iostream>
#include <stack>

typedef int TCheie;
typedef int TValoare;

#include <utility>
typedef std::pair<TCheie, TValoare> TElem;

using namespace std;

class IteratorMDO;

typedef bool(*Relatie)(TCheie, TCheie);

class Nod;
typedef Nod	*PNod;

class Nod {
	friend class MDO;
	TElem e;
	PNod st, dr;
public:
	Nod(TElem e, PNod st, PNod dr);
	TElem element();
	PNod stanga();
	PNod dreata();
};


class MDO {
	friend class IteratorMDO;
private:
	PNod rad;
	PNod adauga_rec(PNod p, TElem e);
	void distrug_rec(PNod p);
	PNod sterge_rec(PNod p, TElem e);
	int dim_rec(PNod p) const ;
	PNod minim(PNod p);

	Relatie rel;

public:

	// constructorul implicit al MultiDictionarului Ordonat
	MDO(Relatie r);

	// adauga o pereche (cheie, valoare) in MDO
	void adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza vectorul de valori asociate
	vector<TValoare> cauta(TCheie c) const;

	//sterge o cheie si o valoare 
	//returneaza adevarat daca s-a gasit cheia si valoarea de sters
	bool sterge(TCheie c, TValoare v);

	//returneaza numarul de perechi (cheie, valoare) din MDO 
	int dim() const;

	//verifica daca MultiDictionarul Ordonat e vid 
	bool vid() const;

	// se returneaza iterator pe MDO
	// iteratorul va returna perechile in ordine in raport cu relatia de ordine
	IteratorMDO iterator() const;

	// destructorul 	
	~MDO();

};
