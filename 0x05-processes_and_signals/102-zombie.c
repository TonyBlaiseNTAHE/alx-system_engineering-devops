#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
/**
 * infinite_while - infinite loop
 *
 * Return: Always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main function
 *
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t  zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
		{
			exit(0);
		}
		else if (zombie < 0)
		{
			perror("fork");
			exit(1);
		}
		else
		{
			printf("Zombie process created, PID: %u\n", zombie);
		}
	}
	infinite_while();
	return (0);
}
