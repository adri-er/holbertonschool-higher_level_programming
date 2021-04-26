#include "lists.h"

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

	list = list->next;
	while (list)
	{
		ans = compare_string((char *)list, (char *)copy);
		if (ans)
		{
			return (1);
		}
		list = list->next;
	}
	return (ans);
}

/**
 * compare_string - compares two strings.
 * @str1: string 1.
 * @str2: string 2.
 *
 * Return: 1 if same, 0 instead.
 */
int compare_string(char *str1, char *str2)
{
	while (*str1 != '\0' && *str2 != '\0')
	{
		if (*str1 != *str2)
		{
			return (0);
		}
		str1++;
		str2++;
	}
	return (1);
}
