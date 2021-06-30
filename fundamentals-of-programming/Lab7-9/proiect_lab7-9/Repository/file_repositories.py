from Repository.repo_student import  RepositoryException2, Student
from Repository.repo_nota import  RepositoryException3, Nota, DTONota
from Repository.repo_disciplina import  RepositoryException1, Disciplina
import unittest


class FileRepoStudent:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_file(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            return []
        rez = []
        linie = f.readline().strip()
        while linie != '':
            at = linie.split("/")
            st = Student(at[0], at[1])
            rez.append(st)
            linie = f.readline().strip()
        f.close()
        return rez

    def all(self):
        return self.load_file()

    def size(self):
        return len(self.load_file())

    def add(self, stud):
        lista = self.load_file()
        if stud in lista:
            raise RepositoryException2()
        lista.append(stud)
        self.add_file(lista)

    def add_file(self, lista):
        with open(self.file_name, 'w') as f:
            for st in lista:
                strf = st.get_id() + "/" + st.get_nume()
                strf = strf + "\n"
                f.write(strf)

    def remove_all(self):
        self.add_file([])

    def delete(self, id):
        lista = self.load_file()
        poz = -1
        for i in range(len(lista)):
            if lista[i].get_id() == id:
                poz = i
        del lista[poz]
        self.add_file(lista)

    def update(self, idi, id, nume):
        lista = self.load_file()
        st = Student(idi, "")
        try:
            lista.remove(st)
            stn = Student(id, nume)
            lista.append(stn)
        except ValueError:
            pass

        self.add_file(lista)


class FileRepoDisciplina:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_file(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            return []
        rez = []
        linie = f.readline().strip()
        while linie != '':
            at = linie.split("/")
            dis = Disciplina(at[0], at[1], at[2])
            rez.append(dis)
            linie = f.readline().strip()
        f.close()
        return rez

    def all(self):
        return self.load_file()

    def size(self):
        return len(self.load_file())

    def add(self, d):
        lista = self.load_file()
        if d in lista:
            raise RepositoryException1
        lista.append(d)
        self.add_file(lista)

    def add_file(self, lista):
        with open(self.file_name, 'w') as f:
            for d in lista:
                drf = d.get_id() + "/" + d.get_nume() + "/" + d.get_profesor()
                drf = drf + "\n"
                f.write(drf)

    def remove_all(self):
        self.add_file([])

    def delete(self, id):
        lista = self.load_file()
        poz = -1
        for i in range(len(lista)):
            if lista[i].get_id() == id:
                poz = i
        del lista[poz]
        self.add_file(lista)

    def update(self, idi , id, nume, prof):
        lista = self.load_file()
        try:
            lista.remove(Disciplina(idi, "", ""))
            d = Disciplina(id, nume, prof)
            lista.append(d)
        except ValueError:
            pass
        self.add_file(lista)


class FileRepoNota:
    def __init__(self, file_name, rep_s, rep_d):
        self.rep_s = rep_s
        self.rep_d = rep_d
        self.file_name = file_name

    def load_file(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            return []
        rez = []
        linie = f.readline().strip()
        while linie != '':
            at = linie.split("/")
            n = Nota(at[0], at[1], at[2], at[3])
            rez.append(n)
            linie = f.readline().strip()
        f.close()
        return rez

    def all(self):
        return self.load_file()

    def size(self):
        return len(self.load_file())

    def add(self, nota):
        lista = self.load_file()
        if nota in lista:
            raise RepositoryException3
        lista.append(nota)
        self.add_file(lista)

    def add_file(self, lista):
        with open(self.file_name, 'w') as f:
            for nota in lista:
                nnn = nota.get_idn() + '/' + nota.get_ids() + '/' + nota.get_idd() + '/' + nota.get_nota()
                nnn = nnn + "\n"
                f.write(nnn)

    def get_all_ids_of_students(self):
        ids = []
        for st in self.rep_s.all():
            ids.append(st.get_id())
        return ids

    def get_all_ids_of_disc(self):
        ids = []
        for d in self.rep_d.all():
            ids.append(d.get_id())
        return ids

    def medii_for_disc(self, disc):
        """
        Functie ce returneaza media fiecarui student pentru disciplina data
        :param disc:
        :return:
        """
        studs = self.get_all_ids_of_students()
        medii = []
        for st in studs:
            k = 0
            s = 0
            for nota in self.load_file():
                if nota.get_ids() == st and nota.get_idd() == disc:
                    k = k + 1
                    s = s + float(nota.get_nota())
            if k != 0:
                m = s/k
            else:
                m = 0
            medii.append(DTONota(st, m))
        return medii

    def total_medii(self):
        '''
        Functie ce returneaza media tuturor notelor pentru fiecare student
        :return:
        '''
        studs = self.get_all_ids_of_students()
        medii = []
        for st in studs:
            k = 0
            s = 0
            for nota in self.load_file():
                if nota.get_ids() == st:
                    k = k + 1
                    s = s + float(nota.get_nota())
            if k != 0:
                m = s/k
            else:
                m = 0
            medii.append(DTONota(st, m))
        return medii

    def all_by_disc(self, disc):
        """
        Functie ce returneaza toate notele de la o disciplina
        :param disc: id-ul disciplinei precizate
        :return: lista cu notele cerute
        """
        lista = []
        for obj in self.load_file():
            if obj.get_idd() == disc:
                nume = ''
                disciplina = ''
                for st in self.rep_s.all():
                    if st.get_id() == obj.get_ids():
                        nume = st.get_nume()
                for d in self.rep_d.all():
                    if d.get_id() == obj.get_idd():
                        disciplina = d.get_nume() 
                s = DTONota(nume, float(obj.get_nota()))
                lista.append(s)
        return lista


class TestCaseFileStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        rep = FileRepoStudent('teststudent.txt')
        try:
            rep.add(Student('1', 'ion'))
            assert True
        except RepositoryException2:
            pass

    def testDelete(self):
        rep = FileRepoStudent('teststudent.txt')
        rep.delete('1')
        self.assertTrue(len(rep.all()) == 0)

    def testUpdate(self):
        rep = FileRepoStudent('teststudent.txt')
        rep.add(Student('1', 'ion'))
        rep.update('1', '1', 'andrei')
        self.assertTrue(rep.all()[0].get_nume() == 'andrei')


class TestCaseFileDisciplina(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        rep = FileRepoDisciplina('testdisciplina.txt')
        try:
            rep.add(Disciplina('001', 'sport', 'hagi'))
            assert True
        except RepositoryException1:
            pass

    def testDelete(self):
        rep = FileRepoDisciplina('testdisciplina.txt')
        rep.delete('001')
        self.assertTrue(len(rep.all()) == 0)

    def testUpdate(self):
        rep = FileRepoDisciplina('testdisciplina.txt')
        rep.add(Disciplina('001', 'sport', 'hagi'))
        rep.update('001', '001' , 'fizica', 'hagi')
        self.assertTrue(rep.all()[0].get_nume() == 'fizica')


class TestCaseFileNota(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)