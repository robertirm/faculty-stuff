#include "IteratorColectie.h"
#include "Colectie.h"

// THETA(N)
IteratorColectie::IteratorColectie(const Colectie& c): col(c) {
	curent = 0;
	deplasare();
}


// THETA(N)
void IteratorColectie::deplasare()
{
	while (curent < col.m and col.e[curent] == NIL)
		curent++;
}


// THETA(N)
void IteratorColectie::prim() {
	curent = 0;
	deplasare();
}


// THETA(N)
void IteratorColectie::urmator() {
	if (valid() == false) throw std::exception();
	curent++;
	deplasare();
}


// O(1)
bool IteratorColectie::valid() const {
	return curent < col.m;
}

// O(1)
TElem IteratorColectie::element() const {
	if (valid() == false) throw std::exception();
	return col.e[curent];
}
