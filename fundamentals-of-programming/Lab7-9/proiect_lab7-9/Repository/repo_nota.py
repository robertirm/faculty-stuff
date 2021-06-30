from Domain.entitate_nota import Nota,DTONota
from Repository.repo_disciplina import RepoDisciplina, Disciplina
from Repository.repo_student import RepoStudent,Student
import unittest


class RepositoryException3(Exception):
    pass


class RepopsitoryStdDisc(Exception):
    pass


class RepoNota:
    def __init__(self, reps, repd):
        """
        Salveaza studentii in memorie
        """
        self.lista = []
        self.rep_s = reps
        self.rep_d = repd

    def add(self, nota):
        """
        Adauga o nota in lista de nota
        :param nota: Nota
        :exception RepoNotaExceptie : o nota cu un id deja existent
        """
        ok1 = 0
        ok2 = 0
        for obj in self.rep_s.all():
            if obj.get_id() == nota.get_ids():
                ok1 = 1

        for obj in self.rep_d.all():
            if obj.get_id() == nota.get_idd():
                ok2 = 1 

        if ok1 == 0 or ok2 == 0:
            raise RepopsitoryStdDisc()
        if nota in self.lista:
            raise RepositoryException3()
        else:
            self.lista.append(nota)

    def size(self):
        """
        Numarul de studenti din memorie
        :return: int
        """
        return len(self.lista)

    def all(self):
        """
        Lista cu toate notele
        :return: list
        """
        return list(self.lista)

    def get_all_ids_of_students(self):
        """
        Functie ce returzeaza o lista cu id-urile tuturor studentilor
        :return:list of strings
        """
        ids = []
        for st in self.rep_s.all():
            ids.append(st.get_id())
        return ids

    def get_all_ids_of_disc(self):
        """
        Functie ce returzeaza o lista cu id-urile tututor disciplinelor
        :return:list of strings
        """
        ids = []
        for d in self.rep_d.all():
            ids.append(d.get_id())
        return ids

    def all_by_disc(self, disc):
        """
        Functie ce returneaza toate notele de la o disciplina
        :param disc: id-ul disciplinei precizate
        :return: lista cu notele cerute
        """
        lista = []
        for obj in self.lista:
            if obj.get_idd() == disc:
                nume = ''
                disciplina = ''
                for st in self.rep_s.all():
                    if st.get_id() == obj.get_ids():
                        nume = st.get_nume()
                for d in self.rep_d.all():
                    if d.get_id() == obj.get_idd():
                        disciplina = d.get_nume()
                nota = float(obj.get_nota())
                s = Nota(obj.get_idn(), nume, disciplina, nota)
                print(type(s.nota))
                lista.append(s)
        return lista

    def medii_for_disc(self, disc):
        """
        Functie ce returneaza media fiecarui student pentru disciplina data
        :return: list
        """
        studs = self.get_all_ids_of_students()
        medii = []
        for st in studs:
            k = 0
            s = 0
            for nota in self.lista:
                if nota.get_ids() == st and nota.get_idd() == disc:
                    k = k + 1
                    s = s + float(nota.get_nota())
            if k != 0:
                m = s/k
            else:
                m = 0
            medii.append(DTONota(st,m))
        return medii

    def total_medii(self):
        '''
        Functie ce returneaza media tuturor notelor pentru fiecare student
        :return: list
        '''
        studs = self.get_all_ids_of_students()
        medii = []
        for st in studs:
            k = 0
            s = 0
            for nota in self.lista:
                if nota.get_ids() == st:
                    k = k + 1
                    s = s + float(nota.get_nota())
            if k != 0:
                m = s/k
            else:
                m = 0
            nota = DTONota(st, m)
            medii.append(nota)
        return medii


class TestCaseRepoNota(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        try:
            rep.add(Nota('01', '11', '1', '5.30'))
            assert True
        except RepositoryException3:
            pass

        try:
            rep.add(Nota('01', '11', '1', '5.30'))
            assert False
        except RepositoryException3:
            pass

    def testMedii1(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        self.assertEqual(rep.medii_for_disc('1')[0].get_student(), '11')
        self.assertEqual(rep.medii_for_disc('1')[1].get_medie(), 4.30)

    def testMedii2(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        self.assertEqual(rep.medii_for_disc('1')[0].get_student(), '11')
        self.assertEqual(rep.medii_for_disc('1')[1].get_medie(), 4.30)

    def testGetAllStudents(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        self.assertTrue(len(rep.get_all_ids_of_students()) == 3)

    def testGetAllDiscipline(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        self.assertTrue(len(rep.get_all_ids_of_disc()) == 1)