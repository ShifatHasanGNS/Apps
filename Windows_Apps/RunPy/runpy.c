// PROGRAM : RunPy (Run_Py) ---> [Python Runner - For Windows]

/*
	AUTHOR  : MD. Shifat Hasan
	Email   : shifathasangns@gmail.com
*/

// START CODING...
// Including necessary header-files...

#include <stdio.h> // It's for standard input & output...
#include <stdlib.h> // It's a standard C-functions's library...
#include <string.h> // It's for dealing with the strings...

// Necessary Functions...

// It checks whether a specific file exists or not...
int does_file_exist(char *fileName);

// It searches for a specific file-name in a list of files...
int find_fileName(char *name);

// It adds '.py' extension at the end of the source-file's name and returns the fullname...
char *filename(char *name);

// It will show some helpful texts...
void help();

// It will show informations about this program(RunPy)...
void info();

// START RUNNING...

// It's the main function from where this program will be started to run...
void main(int argc, char *argv[])
{
	if(argc == 1)
	{
		info();
	}
	else if(argc == 2)
	{
		if(strcmp(argv[1], "help") == 0)
		{
			help();
		}
		else if(strcmp(argv[1], "info") == 0)
		{
			info();
		}
		else if(does_file_exist(filename(argv[1])) == 1)
		{
			char command[100];
			sprintf(command, "pyinstaller --onefile \"%s.py\"", argv[1]);
			system(command);

			*command = '\0';
			sprintf(command, "del \"%s.spec\"", argv[1]);
			system(command);
			*command = '\0';
			sprintf(command, "copy \"dist\\%s.exe\"", argv[1]);
			system(command);
			*command = '\0';
			sprintf(command, "rmdir /q /s dist && rmdir /q /s __pycache__ && rmdir /q /s build");
			system(command);

			system("cls");
			printf("[RunPy] : Running Executable Of --> [%s.py]\n\n", argv[1]);
			*command = '\0';
			sprintf(command, "\"%s\"", argv[1]);
			system(command);
		}

		else
		{
			printf("\n\n [runpy] : Error : '%s.py' doesn't exist... Please try again...\n\n [runpy] : For Help : runpy help\n\n", argv[1]);
		}
	}
    
    else
    {
	    printf("\n\n [runpy] : Error : Please try again...\n\n [runpy] : For Help : runpy help\n\n");
    }
}
// STOP RUNNING...

// Necessary functions are defined here below...

int does_file_exist(char *fileName)
{
	int match;
	char command[111], temp[100];

	sprintf(temp, "%s_temp.txt", fileName);
	sprintf(command, "dir /b > \"%s\"", temp);
	system(command);

	match = find_fileName(fileName);

	*command = '\0';
	sprintf(command, "del \"%s\"", temp);
	system(command);

	return match;
}

int find_fileName(char *name)
{
	int c, match;
	char l[100], line[100], tmp[100];

	sprintf(tmp, "%s_temp.txt", name);
	FILE *temp;
	temp = fopen(tmp, "r");

	while(1)
	{
		c = fgetc(temp);

		if(c == EOF)
		{
			break;
		}

		fseek(temp, -sizeof(char) ,SEEK_CUR);
		fgets(l, 50, temp);
		sscanf(l, "%[^\n]", line);

		if(strcmp(name, line)==0)
		{
			match = 1;
			break;
		}

		else
		{
			match = 0;
		}
	}

	fclose(temp);
	return match;
}

char *filename(char *name)
{
	int len = strlen(name);
	char *fullname;

	fullname = (char *)malloc(sizeof(char)*(len+3));
	sprintf(fullname, "%s.py", name);
	return fullname;
	free(fullname);
}

void help()
{
	printf("\n\n [RunPy] : Syntex : \n\t\t runpy FILENAME\n\t (without '.py' extension)\n\n [RunPy] : Note : You must have 'gcc', python 3', 'pip' and 'pyinstaller' installed...\n\n [RunPy] : How to install the Essential-Tools :\n Read the 'README.txt' file...\n\n [RunPy] : For Informations : runpy info\n\n");
}

void info()
{
	printf("\n\n [RunPy] : INFO :\n\n\tAuthor : MD. Shifat Hasan\n\n RunPy is a program which uses pyinstaller to create executable of a Python Program...\n After creating executable, it instantly removes unnecessary files and copies the main executable file to the source python file's directory...\n After finishing all of these tasks, 'RunPy' runs the executable file...\n\n [RunPy] : Purpose : It will save your time...The executable file will run as fast as a C/C++ program...\n\n [RunPy] : For Help : runpy help\n\n Thanks a lot to use this program... :)\n\n");
}

// END CODING...
