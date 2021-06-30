from UI.console import Consola
from Repository.repo_student import RepoStudent, TestCaseRepoStudent
from Repository.repo_disciplina import RepoDisciplina, TestCaseRepoDisciplina
from Repository.repo_nota import RepoNota,TestCaseRepoNota
from Domain.validator import ValNota, ValStudent, ValDisciplinia, TestCaseValidator
from Service.service_disciplina import SrvDisciplina, TestCaseSrvDisciplina
from Service.service_student import SrvStudent, TestCaseSrvStudent
from Service.service_nota import SrvNota, TestCaseSrvNota
from Domain.entitate_nota import TestCaseNota
from Domain.entitate_student import TestCaseStudent
from Domain.entitate_disciplina import TestCaseDisciplina
import unittest
from Repository.file_repositories import FileRepoStudent, FileRepoDisciplina, FileRepoNota,TestCaseFileStudent,TestCaseFileDisciplina


def teste():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(TestCaseStudent),
        loader.loadTestsFromTestCase(TestCaseDisciplina),
        loader.loadTestsFromTestCase(TestCaseNota),
        loader.loadTestsFromTestCase(TestCaseValidator),
        loader.loadTestsFromTestCase(TestCaseRepoStudent),
        loader.loadTestsFromTestCase(TestCaseRepoDisciplina),
        loader.loadTestsFromTestCase(TestCaseSrvStudent),
        loader.loadTestsFromTestCase(TestCaseSrvDisciplina),
        loader.loadTestsFromTestCase(TestCaseSrvNota),
        loader.loadTestsFromTestCase(TestCaseRepoNota),
        loader.loadTestsFromTestCase(TestCaseFileStudent),
        loader.loadTestsFromTestCase(TestCaseFileDisciplina)
    ))

    runner = unittest.TextTestRunner()
    runner.run(suite)


teste()

rep_s = FileRepoStudent("studenti.txt")
rep_d = FileRepoDisciplina("discipline.txt")
rep_n = FileRepoNota("note.txt", rep_s, rep_d)

"""
rep_s = RepoStudent()
rep_d = RepoDisciplina()
rep_n = RepoNota(rep_s, rep_d)
"""

val_s = ValStudent()
val_d = ValDisciplinia()
val_n = ValNota()

srv_s = SrvStudent(rep_s, val_s)
srv_d = SrvDisciplina(rep_d, val_d)
srv_n = SrvNota(rep_n, val_n)

ui = Consola(srv_s, srv_d, srv_n)

ui.meniu()
