#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: structure with a number and a pointer to the next structure.
 *
 * Return: 0 if theres no cycle, 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list;
	int ans = 0;

	if (!list)
		return (0);

	list = list->next;
	while (list)
	{
		printf("%p : %p\n", (char *)copy, (char *)list);
		ans = compare_string((char *)list, (char *)copy);
		if (ans == 0)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}

/**
 * compare_string - compares two strings.
 * @str1: string 1.
 * @str2: string 2.
 *
 * Return: 0 if same, any other number instead.
 */
int compare_string(char *str1, char *str2)
{
	if (!str1 || !str2)
	{
		return (0);
	}

	while (*str1)
	{
		if (*str1 != *str2)
		{
			break;
		}
		str1++;
		str2++;
	}

	return (*str1 - *str2);
}
