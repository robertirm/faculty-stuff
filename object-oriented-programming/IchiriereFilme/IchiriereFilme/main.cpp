#include "tests.h"
#include "console.h"
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC

void testEverything()
{
	testDomain();
	testRepoFile();
	testRepoInMemory();
	testRepoLab();
	testRepoLabWithExceptions();
	testController();
	testValidator();
	testSearchSortFilter();
	testCart();
	testUndo();
}


int main()
{
	//srand(time(nullptr));

	{
		testEverything();

		std::string fileName = "movies.txt";
		//RepoFile repo(fileName);
		//RepoInMemory repo;
		RepoLab repo(0.5);
		Validator val;
		Controller ctrl{ repo, val };
		Console cons{ ctrl };

		cons.run();
	}

	_CrtDumpMemoryLeaks();
	return 0;
}