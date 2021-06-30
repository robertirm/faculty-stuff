#include "IteratorMDO.h"
#include "MDO.h"
#include <exception>
#include <iostream>

// O(1)
IteratorMDO::IteratorMDO(const MDO& d) : dict(d) {
	this->curent = d.prim;
	IteratorNod* it = new IteratorNod(d.elems[curent]);
	itNod = it;

}

// O(1)
void IteratorMDO::prim(){
	curent = dict.prim;
	IteratorNod* it = new IteratorNod(dict.elems[curent]);
	itNod = it;

}

// O(n)
void IteratorMDO::urmator(){

	if (valid() == false) throw std::exception();

	itNod->urmator();
	

	if (!itNod->valid()) {
		curent = dict.urm[curent];
		if (curent != -1) {
			IteratorNod* it = new IteratorNod(dict.elems[curent]);
			itNod = it;
			

		}
	}
}

// O(1)
bool IteratorMDO::valid() const{
	return curent != -1;
}


// theta(n)
TElem IteratorMDO::element() const{
	if (valid() == false) throw std::exception();

	TCheie c = dict.elems[curent].getCheie();
	TValoare v = itNod->element();

	TElem rez;
	rez.first = c;
	rez.second = v;

	return rez;
}


// O(1)
IteratorNod::IteratorNod(const Nod& nd) : nod(nd) {
	curent = nd.prim;
	
}

// O(1)
void IteratorNod::prim()
{
	curent = nod.prim;

}

// O(1)
void IteratorNod::urmator()
{
	if (valid() == false) throw std::exception();

	curent = nod.urm[curent];
	
}

// O(1)
bool IteratorNod::valid()
{
	return curent != -1;
}

// O(1)
TValoare IteratorNod::element()
{
	if (valid() == false) throw std::exception();
	return nod.elems[curent];
}
