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

	if (list == NULL)
		return (0);

	list = list->next;
	while (list)
	{
		if (copy == list)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
