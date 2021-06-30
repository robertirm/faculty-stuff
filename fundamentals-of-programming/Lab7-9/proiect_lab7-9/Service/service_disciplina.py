from Repository.repo_disciplina import RepositoryException1, RepoDisciplina
from Domain.entitate_disciplina import Disciplina
from Domain.validator import ValDisciplinia
import unittest

class SrvDisciplina:
    def __init__(self, rep, val):
        self.rep = rep
        self.val = val

    def add(self, stud):
        """
        Adauga o disciplina in lista de discipline
        :param disc: Disciplina
        :exception RepoDisciplinaExceptie : o disciplina cu un id deja existent
        """
        self.rep.add(stud)

    def size(self):
        """
        Numarul de discipline din memorie
        :return: int
        """
        return self.rep.size()

    def all(self):
        """
        Lista cu toate disciplinele
        :return: list
        """
        return self.rep.all()

    def delete(self, id):
        """
        sterge o disciplina cu id-ul precizat
        :param id: string
        :return: list
        """
        self.rep.delete(id)

    def update(self, idi, id, nume, prof):
        '''
        Actualizarea unei discipline
        :param idi: id-ul disciplinei curente
        :param id:  id nou
        :param nume: numele nou
        :param prof: profesorul nou
        :return:
        '''
        self.rep.update(idi, id, nume, prof)

    def cautare_id(self, id):
        """
        Cautare a unei discipline dupa ID
        :param id: string
        :return: lista cu disciplinele cautate
        """
        lista = self.all()
        rez = []
        for el in lista:
            if el.get_id() == id:
                rez.append(el)
        return rez

    def cautare_nume(self, nume):
        """
        Cautare a unei discipline dupa nume
        :param nume: string
        :return: lista cu disciplinele cautate
        """
        lista = self.all()
        rez = []
        for el in lista:
            if el.get_nume() == nume:
                rez.append(el)
        return rez

    def cautare_prof(self, prof):
        """
        Cautare a unei discipline dupa profesor
        :param prof: string
        :return: lista cu disciplinele cautate
        """
        lista = self.all()
        rez = []
        for el in lista:
            if el.get_profesor() == prof:
                rez.append(el)
        return rez


class TestCaseSrvDisciplina(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        d = Disciplina("001", 'mate', 'pitagora')
        rep = RepoDisciplina()
        val = ValDisciplinia()
        srv = SrvDisciplina(rep, val)
        try:
            srv.add(d)
            assert True
        except RepositoryException1 as ex:
            pass

        d1 = Disciplina("001", 'dd', 'dd')
        try:
            srv.add(d1)
            assert False
        except RepositoryException1 as ex:
            pass

    def testSize(self):
        rep = RepoDisciplina()
        val = ValDisciplinia()
        srv = SrvDisciplina(rep, val)
        srv.add(Disciplina("001", 'mate', 'pitagora'))
        srv.add(Disciplina("002", 'rom', 'emi'))
        self.assertTrue(srv.size() == 2)

    def testAll(self):
        rep = RepoDisciplina()
        val = ValDisciplinia()
        srv = SrvDisciplina(rep, val)
        srv.add(Disciplina("001", 'mate', 'pitagora'))
        srv.add(Disciplina("002", 'rom', 'emi'))
        self.assertTrue(len(srv.all()) == 2)

    def testUpdate(self):
        rep = RepoDisciplina()
        val = ValDisciplinia()
        srv = SrvDisciplina(rep, val)
        srv.add(Disciplina("001", 'mate', 'pitagora'))
        srv.update('001', '002', 'm', 'p')
        self.assertEqual(srv.all()[0].get_id(), '002')
        self.assertEqual(srv.all()[0].get_nume(), 'm')
        self.assertEqual(srv.all()[0].get_profesor(), 'p')

    def testDelete(self):
        rep = RepoDisciplina()
        val = ValDisciplinia()
        srv = SrvDisciplina(rep, val)
        srv.add(Disciplina("001", 'mate', 'pitagora'))
        srv.delete('001')
        self.assertTrue(srv.size() == 0)


