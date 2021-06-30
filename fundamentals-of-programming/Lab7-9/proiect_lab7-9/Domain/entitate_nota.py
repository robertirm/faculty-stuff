import unittest


class Nota:
    def __init__(self, idn, ids, idd, nota):
        """
        Functie de creare a unei note
        :param idn: string ( id-ul notei)
        :param ids: string ( id-ul studentului )
        :param idd: string ( id-ul disciplinei )
        :param nota: string ( nota studentului la disciplina)
        """
        self.idn = idn
        self.idd = idd
        self.ids = ids
        self.nota = nota

    def get_ids(self):
        """
        Functia returrneaza id-ul studentului cu nota curenta
        :return: string
        """
        return self.ids

    def get_idd(self):
        """
         Functia returrneaza id-ul disciplinei notei curente
         :return: string
         """
        return self.idd

    def get_idn(self):
        """
         Functia returrneaza id-ul notei
         :return: string
         """
        return self.idn

    def get_nota(self):
        """
        Functia returneaza nota
        :return: string
        """
        return self.nota

    def set_nota(self, new_nota):
        """
        Functie ce seteaza nota
        """
        self.nota = new_nota

    def set_ids(self, new_ids):
        """
        Functie ce seteaza id-ul studentului
        """
        self.ids = new_ids

    def set_idd(self, new_idd):
        """
        Functie ce seteaza id-ul disciplinei
        """
        self.idd = new_idd

    def set_idn(self, new_idn):
        """
        Functie ce seteaza id-ul studentului
        """
        self.idn = new_idn

    def __str__(self):
        return str(self.get_idn()+" "+str(self.get_nota())+" "+self.get_ids()+" "+self.get_idd())

    def __eq__(self, other):
        return self.idn == other.idn


class TestCaseNota(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testInitNota(self):
        #   testeaza creearea unei note
        tn = Nota("11", "211", '001', '7.50')
        self.assertEqual(tn.get_idn(), '11')
        self.assertEqual(tn.get_ids(), '211')
        self.assertEqual(tn.get_idd(), '001')
        self.assertEqual(tn.get_nota(), '7.50')

    def testSetters(self):
        # testeaza setteri
        tn = Nota("11", "211", '001', '7.50')
        tn.set_ids('222')
        self.assertEqual(tn.get_ids(), '222')
        tn.set_idd('002')
        self.assertEqual(tn.get_idd(), '002')
        tn.set_idn('12')
        self.assertEqual(tn.get_idn(), '12')
        tn.set_nota('5.00')
        self.assertEqual(tn.get_nota(), '5.00')

    def testRepresentation(self):
        # testeaza reprezentarea
        tn = Nota("11", "211", '001', '7.50')
        tn1 = Nota("11", "55", '004', '6.50')
        self.assertTrue(tn.__str__() == '11 7.50 211 001')
        self.assertTrue(tn == tn1)


class DTONota:
    def __init__(self, student, medie):
        self.student = student
        self.medie = medie

    def get_student(self):
        return self.student

    def get_medie(self):
        return self.medie

    def __eq__(self, other):
         return (self.student == other.student) and (self.medie == other.medie)

    def __str__(self):
        return str(self.student)+' '+str(self.medie)

    def __gt__(self, other):
        if self.medie > other.medie:
            return True
        else:
            return False