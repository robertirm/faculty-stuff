#pragma once
#include <iostream>
#include <exception>
#include <cmath>
#include <limits>
#include <vector>;


#define NIL INT_MIN
#define CAPACITATE 1000000
typedef int TElem;

class IteratorColectie;

class Colectie
{
	friend class IteratorColectie;

private:
	int m;

	TElem* e;
	int* urm;
	int nrElems;
	int primLiber;

	// actualizare primLiber
	void actPrimLiber();

	// functie de dispersie
	int dispersie(TElem e) const;


public:
		//constructorul implicit
		Colectie();

		//adauga un element in colectie
		void adauga(TElem e);

		//sterge o aparitie a unui element din colectie
		//returneaza adevarat daca s-a putut sterge
		bool sterge(TElem e);

		//verifica daca un element se afla in colectie
		bool cauta(TElem elem) const;

		//returneaza numar de aparitii ale unui element in colectie
		int nrAparitii(TElem elem) const;


		//intoarce numarul de elemente din colectie;
		int dim() const;

		//verifica daca colectia e vida;
		bool vida() const;

		//returneaza un iterator pe colectie
		IteratorColectie iterator() const;

		// destructorul colectiei
		~Colectie();

		void intersectie(const Colectie& b);
};

