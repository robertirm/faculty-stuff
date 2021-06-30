#pragma once

#define NULL_TELEM -1
typedef int TElem;
class Nod;
typedef Nod* Pnod;
class IteratorMultime;

class Nod {
private:
	TElem info;
	Pnod urm;
	Pnod ant;

public:
	friend class Multime;

	// constructorul
	Nod(TElem informatie, Pnod ant, Pnod urm) {
		this->info = informatie;
		this->ant = ant;
		this->urm = urm;
	}

	// obtine adresa urmatorului element din lista
	Pnod urmator() {
		return urm;
	}

	// obtine adresa elementului anterior din lista
	Pnod anterior() {
		return ant;
	}

	TElem informatie() {
		return info;
	}

	

};

class Multime {
	friend class IteratorMultime;

    private:
		/* aici e reprezentarea */
		Pnod primul;

    public:
 		//constructorul implicit
		Multime();

		//adauga un element in multime
		//returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
		bool adauga(TElem e);

		//sterge un element din multime
		//returneaza adevarat daca elementul a existat si a fost sters
		bool sterge(TElem e);

		//verifica daca un element se afla in multime
		bool cauta(TElem elem) const;


		//intoarce numarul de elemente din multime;
		int dim() const;

		//verifica daca multimea e vida;
		bool vida() const;

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();
};




