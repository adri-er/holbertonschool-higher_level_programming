#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: structure with a number and a pointer to the next structure.
 *
 * Return: 0 if theres no cycle, 1 if there is.
 */
int check_cycle(listint_t *list)
{
	const listint_t *turtle = list;
	const listint_t *hare = list;

	if (list == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;
		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
