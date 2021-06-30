import unittest


class Student:
    def __init__(self, id, nume):
        '''
        Functie de creare a unui student
        :param id: string (id-ul studentului)
        :param nume: string (numele studentului)
        '''
        self.id = id
        self.nume = nume

    def get_id(self):
        '''
        Functie ce returneaza ID-ul unui student
        :return: string (id-ul studentului)
        '''
        return self.id

    def get_nume(self):
        '''
        Functie ce returneaza numele unui student
        :return: string (numele studentului)
        '''
        return self.nume

    def __eq__(self, other):
        '''
        Verifica egalitatea dintre doi studenti
        :return: bool (True - daca au acelasi id , False - in caz contrar)
        '''
        return self.id == other.id

    def set_id(self, new_id):
        '''
        Functie ce seteaza id-ul unui student
        :param new_id: string (noul id)
        '''
        self.id = new_id

    def set_nume(self, new_nume):
        '''
        Functie ce seteaza numele unui student
        :param new_nume: string (noul nume)
        '''
        self.nume = new_nume

    def __str__(self):
        """
        Converteste obiectul intr-un string
        :return: string(id,nume separate de un spatiu)
        """
        return str(self.get_id() + " " + self.get_nume())


class TestCaseStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testInitStudent(self):
        '''
        Test pentru creearea unei instante de student
        '''
        tstd = Student('211', 'Andrei')
        self.assertEqual(tstd.get_id(), '211')
        self.assertEqual(tstd.get_nume(), 'Andrei')

    def testSetters(self):
        tstd = Student('211', 'Andrei')
        tstd.set_id("222")
        self.assertTrue(tstd.get_id() == '222')
        tstd.set_nume('Vasile')
        self.assertTrue(tstd.get_nume() == 'Vasile')

    def testRepresentation(self):
        tstd = Student('211', 'Andrei')
        self.assertEqual(tstd.__str__(), '211 Andrei')
