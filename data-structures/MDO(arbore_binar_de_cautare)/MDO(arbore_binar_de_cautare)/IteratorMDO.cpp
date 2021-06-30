#include "IteratorMDO.h"
#include "MDO.h"


// O(h)
IteratorMDO::IteratorMDO(const MDO& d) : dict(d){
	curent = dict.rad;
	nrCurent = 0;
	while (curent != nullptr) {
		stiva.push(curent);
		curent = curent->stanga();
	}

	if (!stiva.empty())
		curent = stiva.top();
}

// O(h)
void IteratorMDO::prim(){
	
	while (!stiva.empty())
		stiva.pop();

	curent = dict.rad;
	nrCurent = 0;
	while (curent != nullptr) {
		stiva.push(curent);
		curent = curent->stanga();
	}

	if (!stiva.empty())
		curent = stiva.top();
}

// O(h)
void IteratorMDO::urmator(){
	nrCurent ++;

	stiva.pop();
	if (curent->dreata() != nullptr) {
		curent = curent->dreata();
		while (curent != nullptr) {
			stiva.push(curent);
			curent = curent->stanga();
		}		
	}
	
	if (!stiva.empty())
		curent = stiva.top();
	else
		curent = nullptr;

}


// O(1)
bool IteratorMDO::valid() const{
	return curent != nullptr;
}

// O(1)
TElem IteratorMDO::element() const{
	return curent->element();
}

/*
	COMPLEXITATE : O(n);


	pre: it un iterator pe un ABC, k un numar intreg
	post: it' va indica cu k valori inapoi

	SUBALGORITM revinoKPasi( it, k)
	|	DACA k <= 0 \/ valid(it) == false ATUNCI
	|	|	@arunca exceptie
	|	SF_DACA
	|
	|	DACA k - nrCurent > 0 ATUNCI
	|	|	curent <- NIL
	|	|	returneaza  
	|	SF_DACA
	|
	|	n <- nrCurent - k
	|	prim(it)
	|
	|	CAT TIMP n != 0 EXECUTA
	|	|	urmator(it);
	|	|	n <- n - 1
	|	SF_CAT_TIMP
	SF_SUBALGORITM 

*/
void IteratorMDO::revinoKPasi(int k)
{
	if (k <= 0 || !valid())
		throw exception();

	if ( k-nrCurent > 0 ) {
		curent = nullptr;
		return;
	}

	int n = nrCurent - k;
	prim();

	while (n) {
		urmator();
		n--;
	}
}


