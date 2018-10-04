#include <cstdio>



int main(int i_iArg_Count, const char * i_lpszArg_Values[])
{
	if (i_iArg_Count == 2)
	{
		FILE * fileOut = fopen(i_lpszArg_Values[1],"wt");
		if (fileOut)
		{
			fprintf(fileOut,"#include<cstdio>\n#include<cstdlib>\n\n\nint main(int i_iArg_Count, const char * i_lpszArg_Values[])\n{\n\n\n\treturn 0;\n}\n");
			fclose(fileOut);
		}
	}
	return 0;
}
