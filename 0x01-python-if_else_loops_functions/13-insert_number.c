#include "lists.h"

/**
 * insert_node - inserts a node to a sorted list.
 * @head: pointer to the head of the list.
 * @number: value of the node to insert.
 *
 * Return: NULL if fails or address of new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *foward, *new, *head_copy = *head;

	if (head == NULL || *head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	while (1)
	{
		if (*head == NULL)
		{
			*head = new;
			new->next = NULL;
			*head = head_copy;
			return (new);
		}
		if ((*head)->next)
		{
			if ((*head)->next->n >= number)
			{
				foward = (*head)->next;
				(*head)->next = new;
				new->next = foward;
				*head = head_copy;
				return (new);
			}
		}
		else
		{
			(*head)->next = new;
			new->next = NULL;
			*head = head_copy;
			return (new);
		}
		*head = (*head)->next;
	}
}
