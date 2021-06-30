#include <assert.h>

#include "MDO.h"
#include "IteratorMDO.h"

#include <exception>
#include <vector>

using namespace std;

bool relatie1(TCheie cheie1, TCheie cheie2) {
    if (cheie1 <= cheie2) {
        return true;
    }
    else {
        return false;
    }
}

void testAll() {
    MDO dictOrd = MDO(relatie1);
    assert(dictOrd.dim() == 0);
    assert(dictOrd.vid());
    dictOrd.adauga(1, 2);
    dictOrd.adauga(1, 3);
    assert(dictOrd.dim() == 2);
    assert(!dictOrd.vid());
    vector<TValoare> v = dictOrd.cauta(1);
    assert(v.size() == 2);
    v = dictOrd.cauta(3);
    assert(v.size() == 0);
    IteratorMDO it = dictOrd.iterator();
    it.prim();
    while (it.valid()) {
        TElem e = it.element();
        it.urmator();
    }
    assert(dictOrd.sterge(1, 2) == true);
    assert(dictOrd.sterge(1, 3) == true);
    assert(dictOrd.sterge(2, 1) == false);
    assert(dictOrd.vid());



    ///////////////////////////

    dictOrd.adauga(1, 2);
    dictOrd.adauga(1, 3);
    dictOrd.adauga(4, 3);
    dictOrd.adauga(5, 3);

    IteratorMDO itt = dictOrd.iterator();

    try
    {
        itt.revinoKPasi(-1);
        assert(false);
    }
    catch (exception)
    {
        assert(true);
    }

    itt.urmator();
    itt.urmator();

    try
    {
        itt.revinoKPasi(2);
        assert(true);
    }
    catch (exception)
    {
        assert(false);
    }

    IteratorMDO itt2 = dictOrd.iterator();
    itt2.prim();

    assert(itt2.element() == itt.element());

    itt.revinoKPasi(10);
    assert(itt.valid() == false);
}

