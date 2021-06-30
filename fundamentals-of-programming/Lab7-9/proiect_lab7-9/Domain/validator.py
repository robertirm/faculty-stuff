from Domain.entitate_student import Student
from Domain.entitate_nota import Nota
from Domain.entitate_disciplina import Disciplina
import unittest


class ValidatorException(BaseException):
    def __init__(self, errors):
        self.errors = errors

    def get_errors(self):
        return self.errors


class ValStudent:
    '''
     validare studenti
    '''

    def validate(self, st):
        errors = []
        if st.get_id() == '':
            errors.append("ID-ul nu poate fi gol!")
        if st.get_nume() == '':
            errors.append("Numele nu poate fi gol!")
        if len(errors) > 0:
            raise ValidatorException(errors)


class ValDisciplinia():
    '''
     validare disciplina
    '''

    def validate(self, ds):
        errors = []
        if ds.get_id() == '':
            errors.append("ID-ul nu poate fi gol!")
        if ds.get_nume() == '':
            errors.append("Numele nu poate fi gol!")
        if ds.get_profesor() == '':
            errors.append("Profesorul nu poate sa fie gol!")
        if len(errors) > 0:
            raise ValidatorException(errors)


class ValNota():
    '''
        Functie ce valideaza o nota
        raise ValidatorException daca id-ul studentului este liber
        raise ValidaotrException daca id-ul disciplinei este liber
        raise ValidatorException daca id-ul notei este liber
        raise ValidatorException daca nota este libera
        raise ValidatorException daca nota este negativa
        raise ValidatorException daca nota este zero
        raise ValidatorException daca nota este mai mare decat 10
        raise ValidatorException daca nota nu este un numar real

        after : daca nu s-a ridicat o exceptie nota este valida
    '''

    def validate(self, nota):
        errors = []
        if nota.get_ids() == '':
            errors.append("Id-ul studentului nu poate fi liber!")
        if nota.get_idd() == '':
            errors.append("Id-ul disciplinei nu poate fi liber!")
        if nota.get_idn() == '':
            errors.append("Id-ul notei nu poate fi liber!")
        if nota.get_nota() == '':
            errors.append("Nota nu poate fi goala!")
        try:
            notanr = float(nota.get_nota())
            if notanr <= 0 or notanr > 10:
                raise ValidatorException(["val nota"])
        except ValueError as msg:
            errors.append("value")
        if len(errors) > 0:
            raise ValidatorException(errors)


class TestCaseValidator(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testValStudnet(self):
        val = ValStudent()
        stud = Student("", "")
        self.assertRaises(ValidatorException, val.validate, stud)
        stud = Student("1", '')
        self.assertRaises(ValidatorException, val.validate, stud)
        stud = Student("", 'andrei')
        self.assertRaises(ValidatorException, val.validate, stud)
        stud = Student("1", 'andrei')
        try:
            val.validate(stud)
            assert True
        except ValidatorException as ex:
            assert len(ex.get_errors()) == 2

    def testValDisciplina(self):
        val = ValDisciplinia()
        d = Disciplina("", '', '')
        self.assertRaises(ValidatorException, val.validate, d)
        d.set_id('001')
        self.assertRaises(ValidatorException, val.validate, d)
        d.set_nume('sport')
        self.assertRaises(ValidatorException, val.validate, d)
        d.set_profesor('hagi')
        try:
            val.validate(d)
            assert True
        except ValidatorException as ex:
            assert len(ex.get_errors()) == 2

    def testValNota(self):
        # white box
        val = ValNota()
        # trece prin primele 4 if-uri
        nota = Nota('', '', '', '')
        self.assertRaises(ValidatorException, val.validate, nota)

        # nota introdusa corect
        nota = Nota('1', '2', '3', '7.50')
        try:
            val.validate(nota)
            assert True
        except ValidatorException as ex:
            assert len(ex.get_errors()) == 2

        # trece prin try:except
        nota.set_nota('55.22')
        self.assertRaises(ValidatorException, val.validate, nota)

    def testValNota2(self):
        # black box
        val = ValNota()
        # raise ValidatorException daca id-ul notei este liber
        nota = Nota('', '2', '3', '4.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca id-ul studentului este liber
        nota = Nota('1', '', '3', '4.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca id-ul disciplinei este liber
        nota = Nota('1', '2', '', '4.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca nota este libera
        nota = Nota('1', '2', '3', '')
        self.assertRaises(ValidatorException, val.validate, nota)

        # nota introdusa corect
        nota = Nota('1', '2', '3', '7.50')
        try:
            val.validate(nota)
            assert True
        except ValidatorException as ex:
            assert len(ex.get_errors()) == 2

        # raise ValidatorException daca nota este zero
        nota = Nota('1', '2', '3', '0.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca nota este negativa
        nota = Nota('1', '2', '3', '-1.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca nota este mai mare decat 10
        nota = Nota('1', '2', '3', '11.00')
        self.assertRaises(ValidatorException, val.validate, nota)

        # raise ValidatorException daca nota nu este un numar real
        nota = Nota('1', '2', '3', 'abc')
        self.assertRaises(ValidatorException, val.validate, nota)
