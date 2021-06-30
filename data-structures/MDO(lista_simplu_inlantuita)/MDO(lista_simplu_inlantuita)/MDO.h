#pragma once

#include <vector>
#include <iostream>
typedef int TCheie;
typedef int TValoare;

#include <utility>
typedef std::pair<TCheie, TValoare> TElem;

using namespace std;

class IteratorMDO;
class IteratorNod;
typedef bool(*Relatie)(TCheie, TCheie);

class Nod {
	// construim o lsi de valori pt fiecare cheie
	friend class MDO;
	friend class IteratorNod;
private:
	TCheie cheie; // cheia

	// lsi cu tablou dinamic
	int cp; // capacitatea
	int n;
	TValoare* elems; // tabloul cu valori
	int* urm; // tabloul pt legaturi
	int prim; // ref. catre primul element al listei
	int primLiber; // ref. catre primul el. din lista spatiului liber
	void redim();

	int aloca() {
		int i = primLiber;
		primLiber = urm[primLiber];
		return i;
	}

	void dealoca(int i) {
		urm[i] = primLiber;
		primLiber = i;
	}

	int creeazaNod(TValoare v) {
		int i = aloca();
		this->elems[i] = v;
		urm[i] = -1;
		return i;
	}


public:
	Nod();
	
	TCheie getCheie() {
		return cheie;
	}

	void adauga(TValoare v);

	bool stergere(TValoare v);

	vector<TValoare> toateValorile();

	IteratorNod iterator() const;

};




class MDO {
	friend class IteratorMDO;
	friend class Nod;
    private:
		Relatie rel;
		int nrElems;

		int cp;
		int n;
		Nod* elems;
		int* urm;
		int prim;
		int primLiber;
		void redim();

		int aloca() {
			int i = primLiber;
			primLiber = urm[primLiber];
			return i;
		}

		void dealoca(int i) {
			urm[i] = primLiber;
			primLiber = i;
		}

		int creeazaNod(Nod v) {
			int i = aloca();
			this->elems[i] = v;
			urm[i] = -1;
			return i;
		}
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


	int adaugaInexistente(MDO& mdo);

};

