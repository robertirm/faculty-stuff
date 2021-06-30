#include "IteratorMultime.h"
#include "Multime.h"
#include <exception>
/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	curent = 0;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
void IteratorMultime::prim() {
	curent = 0;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
void IteratorMultime::urmator() {
	if(valid() == false)
		throw std::exception();
	curent++;
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
TElem IteratorMultime::element() const {
	if (valid() == false)
		throw std::exception();
	return multime.elems[curent];
}

/*
	COMPLEXITATE
	caz favorabil = caz mediu = caz defavorabil = theta(1)
*/
bool IteratorMultime::valid() const {
	return curent < multime.dim();
}
