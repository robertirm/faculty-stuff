from Domain.entitate_disciplina import Disciplina
import unittest


class RepositoryException1(BaseException):
    pass


class RepoDisciplina:
    def __init__(self):
        """
        Salveaza studentii in memorie
        """
        self.lista = []

    def add(self, disc):
        """
        Adauga o disciplina in lista de discipline
        :param disc: Disciplina
        :exception RepoDisciplinaExceptie : o disciplina cu un id deja existent
        """
        if disc in self.lista:
            raise RepositoryException1()
        else:
            self.lista.append(disc)

    def size(self):
        """
        Numarul de discipline din memorie
        :return: int
        """
        return len(self.lista)

    def all(self):
        """
        Lista cu toate disciplinele
        :return: list
        """
        return list(self.lista)

    def delete(self, id):
        """
        sterge o disciplina cu id-ul precizat
        :param id: string
        :return: list
        """
        for i, d in enumerate(self.lista):
            if d.id == id:
                del self.lista[i]

    def update(self, idi, id, nume,prof):
        '''
        Actualizarea unei discipline
        :param idi: id-ul disciplinei curente
        :param id:  id nou
        :param nume: numele nou
        :param prof: profesorul nou
        :return:
        '''
        for i, d in enumerate(self.lista):
            if d.id == idi:
                d.set_id(id)
                d.set_nume(nume)
                d.set_profesor(prof)


class TestCaseRepoDisciplina(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        d = Disciplina('001', 'algebra', 'pitagora')
        rep = RepoDisciplina()
        try:
            rep.add(d)
            assert True
        except RepositoryException1 as ex:
            pass

        d = Disciplina('001', 'hh', 'hh')
        try:
            rep.add(d)
            assert False
        except RepositoryException1 as ex:
            pass

    def testSize(self):
        rep = RepoDisciplina()
        rep.add(Disciplina("002", "Desen", "Grigorescu"))
        rep.add(Disciplina('001', 'Algebra', 'Pitagora'))
        self.assertTrue(rep.size() == 2)

    def testUpdate(self):
        rep = RepoDisciplina()
        rep.add(Disciplina("002", "Desen", "Grigorescu"))
        rep.update('002', '003', 'Des', 'fff')
        self.assertEqual(rep.all()[0].get_id(), '003')
        self.assertEqual(rep.all()[0].get_nume(), 'Des')
        self.assertEqual(rep.all()[0].get_profesor(), 'fff')

    def testDelete(self):
        rep = RepoDisciplina()
        rep.add(Disciplina("002", "Desen", "Grigorescu"))
        rep.delete('002')
        self.assertTrue(rep.size() == 0)