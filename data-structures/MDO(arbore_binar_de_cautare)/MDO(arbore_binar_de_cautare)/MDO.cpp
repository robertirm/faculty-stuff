#include "IteratorMDO.h"
#include "MDO.h"
#include <vector>

#include <exception>
using namespace std;

// O(h)
PNod MDO::adauga_rec(PNod p, TElem e)
{
	if (p == nullptr) {
		p = new Nod(e, nullptr, nullptr);
	}
	else {
		if ( rel(e.first, p->e.first) )
			p->st = adauga_rec(p->st, e);
		else
			p->dr = adauga_rec(p->dr, e);
	}
	return p;
}

// O(h)
void MDO::adauga(TCheie c, TValoare v) {
	rad = adauga_rec(rad, pair<TCheie, TValoare>(c, v));
}

// O(h)
void MDO::distrug_rec(PNod p)
{
	if (p != nullptr) {
		distrug_rec(p->stanga());
		distrug_rec(p->dreata());
		delete p;
	}
}

// O(h)
PNod MDO::sterge_rec(PNod p, TElem e)
{
	if (p == nullptr)
		return nullptr;
	else {
		if (e == p->e) {

			if (p->st != nullptr && p->dr != nullptr) {
				PNod temp = minim(p->dr);
				p->e = temp->e;
				p->dr = sterge_rec(p->dr, p->e);
				
				return p;
			}
			else
			{
				PNod temp = p;
				PNod repl;
				if (p->st == nullptr)
					repl = p->dr;
				else
					repl = p->st;

				delete temp;
				
				return repl;
			}


		}
		else {
			if (rel(e.first, p->e.first)) {
				p->st = sterge_rec(p->st, e);
				
				return p;
			}
			else {
				p->dr = sterge_rec(p->dr, e);
				
				return p;
			}
		}

	}
}

// O(h)
PNod MDO::minim(PNod p)
{
	while (p->st != nullptr)
		p = p->st;

	return p;
}

// O(h)
bool MDO::sterge(TCheie c, TValoare v) {

	int size_ant = dim();
	rad = sterge_rec(rad, TElem(c,v));
	return size_ant == dim() + 1;
}


// O(h)
vector<TValoare> MDO::cauta(TCheie c) const {
	vector<TValoare> v;

	PNod temp = rad;

	while (temp != NULL) {
		if (temp->e.first == c) {
			v.push_back(temp->e.second);
		}
		if (rel(c,temp->e.first))
			temp = temp->st;
		else
			temp = temp->dr;
	}

	return v;
}

// O(1)
MDO::MDO(Relatie r) {
	rel = r;
	rad = nullptr;
}

// O(h)
int MDO::dim_rec(PNod p) const
{
	if (p == nullptr)
		return 0;
	else
		return (dim_rec(p->st) + 1 + dim_rec(p->dr));
}

// O(h)
int MDO::dim() const {
	return dim_rec(rad);;
}

// O(h)
bool MDO::vid() const {
	return dim() == 0;
}

// O(1)
IteratorMDO MDO::iterator() const {
	return IteratorMDO(*this);
}

// O(h)
MDO::~MDO() {
	distrug_rec(rad);
}





// O(1)
Nod::Nod(TElem e, PNod st, PNod dr)
{
	this->e = e;
	this->st = st;
	this->dr = dr;
}

// O(1)
TElem Nod::element()
{
	return e;
}

// O(1)
PNod Nod::stanga()
{
	return st;
}

// O(1)
PNod Nod::dreata()
{
	return dr;
}
