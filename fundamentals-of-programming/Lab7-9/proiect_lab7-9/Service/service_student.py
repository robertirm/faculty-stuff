from Repository.repo_student import RepositoryException2, RepoStudent
from Domain.entitate_student import Student
from Domain.validator import ValStudent
import random
import string
import unittest


class SrvStudent:
    def __init__(self, rep, val):
        self.rep = rep
        self.val = val

    def add(self, stud):
        """
        Adauga un student in lista de studenti
        :param stud: Student
        """
        self.rep.add(stud)

    def size(self):
        """
        Numarul de studenti din memorie
        :return: int
        """
        return self.rep.size()

    def all(self):
        """
        Lista cu toti studentii
        :return: list
        """
        return self.rep.all()

    def delete(self, id):
        """
        sterge un student cu id-ul precizat
        :param id: string
        :return: list
        """
        self.rep.delete(id)

    def update(self, idi, id, nume):
        """
        Actualizarea unui student
        :param idi: id-ul studentului curent
        :param id:  id nou
        :param nume: numele nou
        :return:
        """
        self.rep.update(idi, id, nume)

    def cautare_id(self, id):
        """
        Functia cauta studentul cu id-ul precizat
        :param id: string
        :return: Student

        COMPLEXITATE :
        - ca spatiu:
            Nu se folosesc structuri de date aditionale => O(1)
        - ca timp:
            - caz favorabil:
                Id-ul cautat apare la elementul de pe prima pozitie din lista ,
                se efectueaza un singur pas, T(n) = 1 => O(1)
            - caz defavorabil:
                Id-ul cautat nu apare in elementele din lista,
                se efectueaza n pasi, T(n) = n  => O(n)
            - caz mediu:
                Id-ul apare la oricare element din lista,
                se efectueaza , in medie, n/2 pasi => O(n)
        """

        lista = self.all()
        for el in lista:
            if el.get_id() == id:
                return el
        return None

    def cautare_id_recursiv(self, id, index):
        """
        Functia cauta studentul cu id-ul precizat
        :param id: string
        :param index: int
        :return: Student
        """
        if index > len(self.all())-1:
            return None
        elif self.all()[index].get_id() == id:
            return self.all()[index]
        else:
            return self.cautare_id_recursiv(id, index + 1)

    def cautare_nume(self, nume):
        """
        Functia cauta toti studentii cu numele precizat
        :param nume: string
        :return: lista cu studentii ceruti
        """
        lista = self.all()
        rez = []
        for el in lista:
            if nume in el.get_nume():
                rez.append(el)
        return rez

    def cautare_nume_recursiv(self,  nume, index, rez):
        """
        Functia cauta toti studentii cu numele precizat
        :param nume: string
        :param rez: list
        :param index: int
        :return: lista cu studentii ceruti
        """
        if index > len(self.all()) - 1:
            return rez
        else:
            if nume in self.all()[index].get_nume():
                rez.append(self.all()[index])
            return self.cautare_nume_recursiv(nume, index+1, rez)

    def generare_studenti(self, n):
        """
        Functia genereaza n studenti cu date generate la intamplare
        :param: n - int
        after : se vor introduce cei n studenti generati in colectia de studenti
        """
        for i in range(0, n):
            id = random.randint(1, 100000)
            l_nume = random.randint(5, 12)
            nume = ''.join(random.choices(string.ascii_uppercase, k=l_nume))
            st = Student(str(id), nume)
            self.add(st)


class TestCaseSrvStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        st = Student('1', 'andrei')
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        try:
            srv.add(st)
            assert True
        except RepositoryException2 as ex:
            pass

        st1 = Student('1', 'ana')
        try:
            srv.add(st1)
            assert False
        except RepositoryException2 as ex:
            pass

    def testSize(self):
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        srv.add(Student("1", 'andrei'))
        srv.add(Student("2", 'ana'))
        self.assertTrue(srv.size() == 2)

    def testAll(self):
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        srv.add(Student("1", 'andrei'))
        srv.add(Student("2", 'ana'))
        self.assertTrue(len(srv.all()) == 2)

    def testUpdate(self):
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        srv.add(Student("1", 'andrei'))
        rep.update('1', '2', 'nume')
        self.assertEqual(srv.all()[0].get_id(), '2')
        self.assertEqual(srv.all()[0].get_nume(), 'nume')

    def testDelete(self):
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        srv.add(Student("1", 'andrei'))
        srv.delete('1')
        self.assertTrue(srv.size() == 0)

    def testCautari(self):
        rep = RepoStudent()
        val = ValStudent()
        srv = SrvStudent(rep, val)
        srv.add(Student("1", 'andrei'))
        srv.add(Student("2", 'ana'))
        srv.add(Student("3", 'ana'))
        self.assertTrue(srv.cautare_id('1').get_nume() == 'andrei')
        self.assertTrue(len(srv.cautare_nume('ana')) == 2)


