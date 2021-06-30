#include "IteratorMultime.h"
#include "Multime.h"
#include <exception>

/*
	pre: it - iterator 
	post: curent va indica catre elementul anterior

	subalgoritm anterior(it):
		daca valid(it) = false
			throw exception
			return void
		sfdaca
		daca curent = it.prim
			curent = NIL
			return void
		sfdaca
		curent = curent -> anterior
	sf subalgoritm

	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
void IteratorMultime::anterior() {
	if (valid() == false) throw std::exception();
	if (curent == multime.primul) {
		curent = nullptr; return;
	}
	curent = curent->anterior();
}

/*
	COMPLEXITATE
	---> O(1)
*/
IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	curent = multime.primul;
}

/*
	COMPLEXITATE
	---> O(1)
*/
void IteratorMultime::prim() {
	curent = multime.primul;
}

/*
	COMPLEXITATE
	---> O(1)
*/
void IteratorMultime::urmator() {
	if(valid() == false) throw std::exception();
	curent = curent->urmator();
}


/*
	COMPLEXITATE
	---> O(1)
*/
TElem IteratorMultime::element() const {
	if(valid() == false)
		if (valid() == false) throw std::exception();
	return curent->informatie();
}

/*
	COMPLEXITATE
	---> O(1)
*/
bool IteratorMultime::valid() const {
	return curent != nullptr;
}
