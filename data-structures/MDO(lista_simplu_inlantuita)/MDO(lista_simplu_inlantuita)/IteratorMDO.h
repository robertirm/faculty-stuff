#pragma once

#include "MDO.h"

class IteratorMDO;

class IteratorNod {
	friend class Nod;
private:
	const Nod& nod;
	int curent;

public:
	IteratorNod() = default;
	IteratorNod(const Nod& nod);
	void prim();
	void urmator();
	bool valid();
	TValoare element();
	
};



class IteratorMDO{
	friend class MDO;
	friend class IteratorNod;
private:

	//constructorul primeste o referinta catre Container
	//iteratorul va referi primul element din container
	IteratorMDO(const MDO& d);

	//contine o referinta catre containerul pe care il itereaza
	const MDO& dict;
	
	int curent;
	IteratorNod* itNod;


public:

		//reseteaza pozitia iteratorului la inceputul containerului
		void prim();

		//muta iteratorul in container
		// arunca exceptie daca iteratorul nu e valid
		void urmator();

		//verifica daca iteratorul e valid (indica un element al containerului)
		bool valid() const;

		//returneaza valoarea elementului din container referit de iterator
		//arunca exceptie daca iteratorul nu e valid
		TElem element() const;

		
};


