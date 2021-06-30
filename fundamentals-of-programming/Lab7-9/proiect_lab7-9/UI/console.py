from Repository.repo_student import RepositoryException2, Student
from Repository.repo_disciplina import Disciplina, RepositoryException1
from Repository.repo_nota import RepoNota, RepositoryException3, Nota, RepopsitoryStdDisc
from Domain.validator import ValidatorException


class Consola:
    def __init__(self, srv_s, srv_d, srv_n):
        self.srv_s = srv_s
        self.srv_d = srv_d
        self.srv_n = srv_n

    def meniu(self):
        print("================MENIU==================")
        print("=======Manipulare studenti=======")
        print("show.s - afiseaza toti studentii")
        print("add.s - adauga un student")
        print("del.s - sterge un student dupa id-ul sau")
        print("upd.s - actualizeaza un student")
        print("======Manipulare discipline======")
        print("show.d - afiseaza toate disciplinele")
        print("add.d - adauga o disciplina")
        print("del.d - sterge o disciplina dupa id")
        print("upd.d - actualizeaza o disciplina")
        print("=============Cautari============")
        print("search.s.id - cauta studenti dupa id")
        print("search.s.nume = cauta studenti dupa nume")
        print("search.d.id - cauta discipline dupa id")
        print("search.d.nume - cauta discipline dupa nume")
        print("search.d.prof - cauta discipline dupa profesor")
        print("=======Manipulare note=======")
        print("show.n - afiseaza toate notele")
        print("add.n - adauga o nota")
        print("===========Statistici============")
        print("sort.nume - sortare note pentru o disciplina dupa numele elevilor")
        print("sort.nota - sortare note pentru o disciplina dupa valoarea notelor")
        print("procent - primi 20% din studenți ordonati dupa media notelor la toate disciplinele")
        print("medie - nr de studenti si media totala pentru o disciplina")

        while True:
            cmd = input(">>>")
            if cmd == 'exit':
                break
            elif cmd == 'show.s':
                self.show_studenti()
            elif cmd == 'add.s':
                self.adaugare_student()
            elif cmd == 'del.s':
                self.stergere_student()
            elif cmd == 'upd.s':
                self.update_student()
            elif cmd == 'show.d':
                self.show_discipline()
            elif cmd == 'add.d':
                self.adaugare_disciplina()
            elif cmd == 'del.d':
                self.stergere_disciplina()
            elif cmd == 'upd.d':
                self.update_disciplina()
            elif cmd == 'search.s.id':
                self.cautare_student_id()
            elif cmd == 'search.s.nume':
                self.cautare_student_nume()
            elif cmd == 'search.d.id':
                self.cautare_disciplina_id()
            elif cmd == 'search.d.nume':
                self.cautare_disciplina_nume()
            elif cmd == 'search.d.prof':
                self.cautare_disciplina_prof()
            elif cmd == 'add.n':
                self.adaugare_nota()
            elif cmd == 'show.n':
                self.show_note()
            elif cmd == 'del.n':
                self.stergere_note()
            elif cmd == 'sort.nume':
                self.sortare_note_nume()
            elif cmd == 'sort.nota':
                self.sortare_note_nota()
            elif cmd == 'procent':
                self.procent()
            elif cmd == 'exemplu':
                self.exemplu()
            elif cmd == 'medie':
                self.media_disciplinei()
            elif 'generate' in cmd:
                self.generare_studenti(cmd)
            else:
                print("Comanda Invalida !")

    def show_studenti(self):
        sts = self.srv_s.all()
        print("Studentii sunt :")
        if not sts:
            print("Nu exista studenti!")
        else:
            for st in sts:
                print(st)

    def adaugare_student(self):
        print("Introduceti datele noului student.")
        i = input("ID : ")
        nume = input("Nume : ")
        st = Student(i, nume)
        try:
            self.srv_s.val.validate(st)
            self.srv_s.add(st)
        except ValidatorException as msg:
            print("Nu este valid!")
        except RepositoryException2 as msg:
            print("Id nepotrivit!")

    def stergere_student(self):
        print("Introduceti id-ul studentului pe care doriti sa-l stergeti")
        id = input("ID : ")
        self.srv_s.delete(id)
        print("S-au sters!")

    def update_student(self):
        print("Introduceti id-ul studentului pe care doriti sa-l modificati")
        ido = input("ID : ")
        print("Introduceti noile date: ")
        id = input("ID : ")
        nume = input("Nume : ")
        st = Student(id, nume)
        try:
            self.srv_s.val.validate(st)
            self.srv_s.update(ido, id, nume)
        except ValidatorException as msg:
            print("Nu este valid!")
        except RepositoryException2 as msg:
            print("Id nepotrivit!")
        print("S-a actualizatat!")

    def show_discipline(self):
        dis = self.srv_d.all()
        print("Disciplinele sunt :")
        if not dis:
            print("Nu exista discipline!")
        else:
            for d in dis:
                print(d)

    def adaugare_disciplina(self):
        print("Introduceti datele noii discipline.")
        i = input("ID : ")
        nume = input("Nume : ")
        prof = input("Profesor: ")
        d = Disciplina(i, nume, prof)
        try:
            self.srv_d.val.validate(d)
            self.srv_d.add(d)
        except ValidatorException as msg:
            print("Nu este valid!")
        except RepositoryException1 as msg:
            print("Id nepotrivit!")

    def stergere_disciplina(self):
        print("Introduceti id-ul disciplinei pe care doriti sa o stergeti")
        id = input("ID : ")
        self.srv_d.delete(id)
        print("S-au sters!")

    def update_disciplina(self):
        print("Introduceti id-ul disciplinei pe care doriti sa o modificati")
        ido = input("ID : ")
        print("Introduceti noile date: ")
        id = input("ID : ")
        nume = input("Nume : ")
        prof = input("Profesor :")
        d = Disciplina(id, nume, prof)
        try:
            self.srv_d.val.validate(d)
            self.srv_d.update(ido, id, nume, prof)
        except ValidatorException as msg:
            print("Nu este valid!")
        except RepositoryException1 as msg:
            print("Id nepotrivit!")
        print("S-a actualizatat!")

    def cautare_student_id(self):
        print("Introduceti id-ul studentului cautat. ")
        i = input("ID : ")
        # rez = self.srv_s.cautare_id(i)
        rez = self.srv_s.cautare_id_recursiv(i, 0)
        if rez is None:
            print("Nu exista astfel de studenti!")
        else:
            print(rez)

    def cautare_student_nume(self):
        print("Introduceti numele studentului cautat.")
        num = input("Nume : ")
        # rez = self.srv_s.cautare_nume(num)
        rez = self.srv_s.cautare_nume_recursiv(num, 0, [])
        if not rez:
            print("Nu exista astfel de studenti!")
        else:
            for el in rez:
                print(el)

    def cautare_disciplina_nume(self):
        print("Introduceti numele disciplinei cautate.")
        i = input("Nume : ")
        rez = self.srv_d.cautare_nume(i)
        if not rez:
            print("Nu exista astfel de discipline!")
        else:
            for el in rez:
                print(el)

    def cautare_disciplina_id(self):
        print("Introduceti id-ul disciplinei cautate.")
        i = input("ID : ")
        rez = self.srv_d.cautare_id(i)
        if not rez:
            print("Nu exista astfel de discipline!")
        else:
            for el in rez:
                print(el)

    def cautare_disciplina_prof(self):
        print("Introduceti profesorul disciplinei cautate.")
        i = input("Profesor : ")
        rez = self.srv_d.cautare_prof(i)
        if not rez:
            print("Nu exista astfel de discipline!")
        else:
            for el in rez:
                print(el)

    def generare_studenti(self, cmd):
        arg = cmd.split(' ')
        param = arg[1]
        try:
            param = int(param)
        except ValueError as msg:
            print("Valoare invalida!")
        self.srv_s.generare_studenti(param)
        print("S-au generat!")

    def adaugare_nota(self):
        print("Introduceti datele noii note.")
        idn = input(" ID Nota :")
        ids = input(" ID Student : ")
        idd = input(" ID Disciplina : ")
        nota = input(" Nota : ")
        n = Nota(idn, ids, idd, nota)
        try:
            self.srv_n.val.validate(n)
            self.srv_n.add(n)
        except ValidatorException as msg:
            print("Nu este valid!")
        except RepositoryException3 as msg:
            print("ID nota nepotrivit!")
        except RepopsitoryStdDisc as msg:
            print("Studentul sau disciplina precizata nu exista!")
        else:
            print("S-a adaugat!")

    def show_note(self):
        nts = self.srv_n.all()
        print("Notele sunt :")
        if not nts:
            print("Nu exista note!")
        else:
            for n in nts:
                print(n)

    def stergere_note(self):
        print("Introduceti id-ul notei pe care doriti sa o stergeti")
        id = input("ID : ")
        self.srv_n.delete(id)
        print("S-a sters!")

    def sortare_note_nume(self):
        print("Introduceti id-ul disciplinei pentru care doriti notele.")
        d = input("ID Disciplina : ")
        l = self.srv_n.sortare_dupa_nume(d)
        if not l:
            print("Nu exista!")
        for obj in l:
            print(obj)

    def sortare_note_nota(self):
        print("Introduceti id-ul disciplinei pentru care doriti notele.")
        d = input("ID Disciplina : ")
        l = self.srv_n.sortare_dupa_nota(d)
        if not l:
            print("Nu exista!")
        for obj in l:
            print(obj)

    def procent(self):
        print("Top 20% :")
        medii = self.srv_n.procent()
        if len(medii) == 0:
            print("Nu exista!")
        else:
            for i in medii:
                nume = ""
                for name in self.srv_s.rep.all():
                    if i.get_student() == name.get_id():
                        nume = name.get_nume()
                print(nume, ' ', i.get_medie())

    def media_disciplinei(self):
        print("Introduceti id-ul disciplinei dorite:")
        i = input("ID : ")
        nr_std, medie = self.srv_n.media_disc(i)
        print("Numarul de studenti este : ", nr_std)
        print("Media disciplinei este : ", medie)

    def exemplu(self):
        # exemple elevi
        self.srv_s.add(Student('211', 'Maria'))
        self.srv_s.add(Student('212', 'Andrei'))
        self.srv_s.add(Student('213', 'Ionut'))
        self.srv_s.add(Student('214', 'Ana'))
        self.srv_s.add(Student('215', 'Ovidiu'))
        self.srv_s.add(Student('216', 'Cosmin'))


        # exemple discipline
        self.srv_d.add(Disciplina('001', 'Matematica', 'Pitagora'))
        self.srv_d.add(Disciplina('002', 'Romana', 'Eminescu'))
        self.srv_d.add(Disciplina('003', 'Sport', 'Hagi'))
        self.srv_d.add(Disciplina('004', 'Istorie', 'Tepes'))

        # exemple note
        self.srv_n.add(Nota('11', '211', '001', '9.30'))
        self.srv_n.add(Nota('12', '211', '002', '7.50'))
        self.srv_n.add(Nota('13', '211', '003', '10.00'))
        self.srv_n.add(Nota('14', '211', '004', '9.30'))

        self.srv_n.add(Nota('21', '212', '001', '5.30'))
        self.srv_n.add(Nota('22', '212', '002', '7.00'))
        self.srv_n.add(Nota('23', '212', '003', '9.00'))
        self.srv_n.add(Nota('24', '212', '004', '6.30'))

        self.srv_n.add(Nota('31', '213', '001', '7.50'))
        self.srv_n.add(Nota('32', '213', '002', '8.00'))
        self.srv_n.add(Nota('33', '213', '003', '10.00'))
        self.srv_n.add(Nota('34', '213', '004', '8.60'))

        self.srv_n.add(Nota('41', '214', '001', '10.00'))
        self.srv_n.add(Nota('42', '214', '002', '9.00'))
        self.srv_n.add(Nota('43', '214', '003', '6.00'))
        self.srv_n.add(Nota('44', '214', '004', '4.50'))

        self.srv_n.add(Nota('51', '215', '001', '7.50'))
        self.srv_n.add(Nota('52', '215', '002', '9.00'))
        self.srv_n.add(Nota('53', '215', '003', '9.50'))
        self.srv_n.add(Nota('54', '215', '004', '7.50'))

        print("Exemplu introdus!")
