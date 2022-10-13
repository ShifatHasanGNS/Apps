#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    if (argc == 1 || (argc == 2 && (!strcmp(argv[1], "-h") || !strcmp(argv[1], "help"))))
    {
        printf("\n*** Hello! I'm Gen (Generator). I can create, build and run only C++ source files.\n\n*** You can use me for quick testing purpose. \n\n");
        printf("+------------------------------------------------------------------------------------------------------------------------------------+\n");
        printf("| # |                Commands                         |                                 What it does?                                |\n");
        printf("|---|-------------------------------------------------|------------------------------------------------------------------------------|\n");
        printf("| 1 | ./gen  or  ./gen -h  or  ./gen help             | Shows the exact thing you're watching now                                    |\n");
        printf("|---|-------------------------------------------------|------------------------------------------------------------------------------|\n");
        printf("| 2 | ./gen -n <filename>  or  ./gen new <filename>   | Creates a new new file named <filename>.cpp and writes some boilerplate code |\n");
        printf("|---|-------------------------------------------------|------------------------------------------------------------------------------|\n");
        printf("| 3 | ./gen -t <filename>  or  ./gen test <filename>  | Runs: g++ -std=c++20 -Wall -g -o0 <filename>.cpp -o test                     |\n");
        printf("|---|-------------------------------------------------|------------------------------------------------------------------------------|\n");
        printf("| 3 | ./gen -b <filename>  or  ./gen build <filename> | Runs: g++ -std=c++20 -Wall -g0 -o2 <filename>.cpp -o <filename>              |\n");
        printf("+------------------------------------------------------------------------------------------------------------------------------------+\n\n");
        return 0;
    }

    else if (argc == 3)
    {
        if (!strcmp(argv[1], "-n") || !strcmp(argv[1], "new"))
        {
            char *filename = (char *)calloc(64, sizeof(char));
            sprintf(filename, "%s.cpp", argv[2]);
            FILE *fp = fopen(filename, "w");

            if (fp == NULL)
            {
                printf("\n GEN : [ERROR] : Could not create or write to the file '%s.cpp'. So, please try another name.\n\n *** For help --> Type: ./gen\n\n", argv[2]);
                fclose(fp);
                return 0;
            }
            fprintf(fp, "// filename: %s.cpp\n#include <bits/stdc++.h>\n\nint main()\n{\n    // c++ code...\n\n    return 0;\n}\n\n", argv[2]);
            fclose(fp);
            printf("\n GEN : [SUCCESS] : '%s.cpp' is created successfully.\n\n", argv[2]);
        }

        else if (!strcmp(argv[1], "-t") || !strcmp(argv[1], "test"))
        {
            char *filename = (char *)calloc(64, sizeof(char));
            sprintf(filename, "%s.cpp", argv[2]);
            if (fopen(filename, "r") != NULL)
            {
                printf("\n GEN : [RUNNING] : g++ -std=c++20 -Wall -g -o0 %s.cpp -o test", argv[2]);
                char *command = (char *)calloc(128, sizeof(char));
                sprintf(command, "g++ -std=c++20 -Wall -g -o0 %s.cpp -o test", argv[2]);
                system(command);
                printf("\n GEN : [SUCCESS] : From '%s.cpp', (including debug-symbols) an unoptimized binary named 'test' is created successfully (to test).\n\n", argv[2]);
            }
            else
                printf("\n GEN : [Wrong Command] : '%s.cpp' does not exist.\n\n *** For help --> Type: ./gen\n\n", argv[2]);
        }

        else if (!strcmp(argv[1], "-b") || !strcmp(argv[1], "build"))
        {
            char *filename = (char *)calloc(64, sizeof(char));
            sprintf(filename, "%s.cpp", argv[2]);
            if (fopen(filename, "r") != NULL)
            {
                printf("\n GEN : [RUNNING] : g++ -std=c++20 -Wall -g0 -o2 %s.cpp -o %s", argv[2], argv[2]);
                char *command = (char *)calloc(128, sizeof(char));
                sprintf(command, "g++ -std=c++20 -Wall -g0 -o2 %s.cpp -o %s", argv[2], argv[2]);
                system(command);
                printf("\n GEN : [SUCCESS] : From '%s.cpp', an optimized binary named '%s' is created successfully (to use).\n\n", argv[2], argv[2]);
            }
            else
                printf("\n GEN : [Wrong Command] : '%s.cpp' does not exist.\n\n *** For help --> Type: ./gen\n\n", argv[2]);
        }
    }

    else
        printf("\n GEN : [Wrong Command] : Please try again. For help, type: ./gen\n\n");
    
    return 0;
}