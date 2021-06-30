from Domain.entitate_student import Student
import unittest


class RepositoryException2(Exception):
    pass


class RepoStudent:
    def __init__(self):
        """
        Salveaza studentii in memorie
        """
        self.lista = []

    def add(self, stud):
        """
        Adauga un student in lista de studenti
        :param stud: Student
        """
        if stud in self.lista:
            raise RepositoryException2()
        else:
            self.lista.append(stud)

    def size(self):
        """
        Numarul de studenti din memorie
        :return: int
        """
        return len(self.lista)

    def all(self):
        """
        Lista cu toti studentii
        :return: list
        """
        return self.lista

    def delete(self, id):
        """
        sterge un student cu id-ul precizat
        :param id: string
        :return: list
        """
        for i, st in enumerate(self.lista):
            if st.get_id() == id:
                del self.lista[i]

    def delete_recursiv(self, id, i):
        pass


    def update(self, idi, id, nume):
        '''
        Actualizarea unui student
        :param idi: id-ul studentului curent
        :param id:  id nou
        :param nume: numele nou
        :return:
        '''
        for i, st in enumerate(self.lista):
            if st.id == idi:
                st.set_id(id)
                st.set_nume(nume)


class TestCaseRepoStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        st = Student('1', 'andrei')
        rep = RepoStudent()
        try:
            rep.add(st)
            assert True
        except RepositoryException2 as ex:
            pass

        st1 = Student('1', 'ana')
        try:
            rep.add(st1)
            assert False
        except RepositoryException2 as ex:
            pass

    def testSize(self):
        rep = RepoStudent()
        rep.add(Student("1", 'andrei'))
        rep.add(Student("2", 'ana'))
        self.assertTrue(rep.size() == 2)

    def testAll(self):
        rep = RepoStudent()
        rep.add(Student("1", 'andrei'))
        rep.add(Student("2", 'ana'))
        self.assertTrue(len(rep.all()) == 2)

    def testUpdate(self):
        rep = RepoStudent()
        rep.add(Student("1", 'andrei'))
        rep.update('1', '2', 'nume')
        self.assertEqual(rep.all()[0].get_id(), '2')
        self.assertEqual(rep.all()[0].get_nume(), 'nume')

    def testDelete(self):
        rep = RepoStudent()
        rep.add(Student("1", 'andrei'))
        rep.delete('1')
        self.assertTrue(rep.size() == 0)