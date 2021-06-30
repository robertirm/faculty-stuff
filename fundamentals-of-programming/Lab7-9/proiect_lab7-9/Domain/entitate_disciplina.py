import unittest


class Disciplina:
    def __init__(self , id , nume, profesor):
        """
        Functie de creare a unei discipline
        :param id: string (id-ul disciplinei)
        :param nume: string (numele disciplinei)
        :param profesor: string (profesorul disciplinei)
        """
        self.id = id
        self.nume = nume
        self.profesor = profesor

    def get_id(self):
        """
        Functie ce returneaza id-ul unei discipline
        :return: string  (id-ul disciplinei)
        """
        return self.id

    def get_nume(self):
        """
        Functie ce returneaza numele unei discipline
        :return: string  (numele disciplinei)
        """
        return self.nume

    def get_profesor(self):
        """
        Functie ce returneaza profesorul unei discipline
        :return: string  (profesorul disciplinei)
        """
        return self.profesor

    def __eq__(self, other):
        """
        Verifica egalitatea dintre doua discipline
        :return: bool (True - daca au acelasi id , False - in caz contrar)
        """
        return self.id == other.id

    def set_id(self, new_id):
        '''
        Functie ce seteaza id-ul unei discipline
        :param new_id: string (noul id)
        '''
        self.id = new_id

    def set_nume(self, new_nume):
        '''
        Functie ce seteaza numele unei discipline
        :param new_nume: string (noul nume)
        '''
        self.nume = new_nume

    def set_profesor(self, new_prof):
        '''
        Functie ce seteaza numele unei discipline
        :param new_prof: string (noul profesor)
        '''
        self.profesor = new_prof

    def __str__(self):
        """
        Converteste obiectul intr-un string
        :return: string (id,nume,profesor separate de un spatiu)
        """
        return str(self.get_id()+" "+self.get_nume()+" "+self.get_profesor())


class TestCaseDisciplina(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testInitDisciplna(self):
        #   testeaza creearea unei discipline
        td = Disciplina("001", 'sport', 'hagi')
        self.assertEqual(td.get_id(), '001')
        self.assertEqual(td.get_nume(), 'sport')
        self.assertEqual(td.get_profesor(), 'hagi')

    def testSetters(self):
        #   testeaza setteri
        td = Disciplina("001", 'sport', 'hagi')
        td.set_id('002')
        self.assertEqual(td.get_id(), '002')
        td.set_nume('ed fizica')
        self.assertEqual(td.get_nume(), 'ed fizica')
        td.set_profesor('mutu')
        self.assertEqual(td.get_profesor(), 'mutu')

    def testRepresentation(self):
        #   testeaza reprezentarea
        td = Disciplina("001", 'sport', 'hagi')
        self.assertTrue(td.__str__() == '001 sport hagi')
        td1 = Disciplina('001', 'ggg', 'ggg')
        self.assertTrue(td == td1)