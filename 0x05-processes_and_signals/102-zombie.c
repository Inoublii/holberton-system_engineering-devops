#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - infinite loop
 * Return: 0
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
 * main - create zombies
 * Return: 0
 */
int main(void)
{
int i = 1;
pid_t pid;

while (i <= 5)
{
pid = fork();
if (pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
exit(0);
}
i += 1;
}
infinite_while();
return (0);
}
