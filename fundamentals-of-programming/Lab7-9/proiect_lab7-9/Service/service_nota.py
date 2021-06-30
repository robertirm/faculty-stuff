from Domain.entitate_nota import Nota, DTONota
from Domain.validator import ValNota
from Domain.entitate_student import Student
from Domain.entitate_disciplina import Disciplina
from Repository.repo_nota import RepoNota
from Repository.repo_disciplina import RepoDisciplina
from Repository.repo_student import RepoStudent
from sorting import shell_sort, bubble_sort, cmp_combinat
import unittest


class SrvNota:
    def __init__(self, rep, val):
        self.rep = rep
        self.val = val

    def add(self, stud):
        """
        Adauga o nota in lista de note
        :param disc: nota
        :exception RepoNotaExceptie : o nota cu un id deja existent
        """
        self.rep.add(stud)

    def size(self):
        """
        Numarul de note din memorie
        :return: int
        """
        return self.rep.size()

    def all(self):
        """
        Lista cu toate notele
        :return: list
        """
        return self.rep.all()

    def delete(self, id):
        """
        sterge o nota cu id-ul precizat
        :param id: string
        :return: list
        """
        self.rep.delete(id)

    def update(self, idn, ids, idd, nota):
        """
        Actualizeaza o nota
        :param idn: id-ul notei
        :param ids: id-ul studentului
        :param idd: id-ul disciplinei
        :param nota: valoarea notei
        :return: se actualizeaza nota respectiva
        """
        self.rep.update(idn, ids, idd, nota)

    def sortare_dupa_nume(self, disc):
        """
        Sorteaza notele pentru o disciplina dupa numele studentilor , in ordine alfabetica
        :param disc: disciplina precizata (string)
        :return: list
        """
        srt = self.rep.all_by_disc(disc)
        # newlist = sorted(srt, key=lambda x: x.student)
        # newlist = bubble_sort(srt, key=lambda x: x.student)
        newlist = shell_sort(srt, key=lambda x: x.student)

        return newlist

    def sortare_dupa_nota(self, disc):
        """
        Sorteaza notele pentru o disciplina dupa valoarea notei , in ordine descrescatoare
        :param disc: disciplina precizata (string)
        :return: list
        """
        srt = self.rep.all_by_disc(disc)
        # newlist = sorted(srt, key=lambda x: x, reverse=True)
        # newlist = bubble_sort(srt, key=lambda x: x.medie, reverse=True)
        # newlist = shell_sort(srt, key=lambda x: x.medie, reverse=True)
        # newlist = bubble_sort(srt, cmp=cmp_combinat, reverse=True)
        newlist = shell_sort(srt, cmp=cmp_combinat, reverse=True)

        return newlist

    def procent(self):
        '''
        Selecteaza primii 20% dintre studenti dupa media notelor ordonate crescator
        :return:
        '''
        medii = self.rep.total_medii()
        newlist = sorted(medii, key=lambda x: x.medie, reverse=True)
        n = len(medii)
        n = int(round(n * 0.2))
        medii_perc = newlist[:n]
        return medii_perc

    def media_disc(self, id_d):
        """
        Functia afla nr de studenti si 'media disciplinei' pentru o disciplina specificata
        :param id_d: id-ul disciplinei (string)
        :return: nr_studenti - int , media - float
        """
        medii = self.rep.medii_for_disc(id_d)
        suma = 0
        k = 0
        for m in medii:
            if m[1] != 0:
                suma = suma + m[1]
                k = k + 1

        if k == 0:
            media = 0
        else:
            media = suma / k

        return k, media


class TestCaseSrvNota(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testProcent(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        val = ValNota()
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        srv = SrvNota(rep, val)
        self.assertEqual(srv.procent()[0].get_medie(), 8.30)

    def testSortareNume(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        val = ValNota()
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        srv = SrvNota(rep, val)
        # self.assertEqual(srv.sortare_dupa_nume('1')[0].student, 'ana')

    def testSortareNota(self):
        rs = RepoStudent()
        rd = RepoDisciplina()
        rep = RepoNota(rs, rd)
        val = ValNota()
        rs.add(Student('11', 'andrei'))
        rs.add(Student('12', 'ana'))
        rs.add(Student('13', 'vasile'))
        rd.add(Disciplina('1', 'mate', 'pitagora'))
        rep.add(Nota('01', '11', '1', '5.30'))
        rep.add(Nota('02', '12', '1', '4.30'))
        rep.add(Nota('03', '13', '1', '8.30'))
        rep.add(Nota('04', '11', '1', '9.30'))
        srv = SrvNota(rep, val)
        # self.assertEqual(srv.sortare_dupa_nota('1')[0].student, 'andrei')
