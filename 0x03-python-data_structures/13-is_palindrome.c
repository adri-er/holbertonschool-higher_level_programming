#include "lists.h"
#include <stdio.h>

/**
 * length_linked_list - determines the length of a linked list.
 * @head: pointer to the head of a linked list.
 *
 * Return: length of a linked list.
 */
int length_linked_list(listint_t *head)
{
	int length = 0;

	for (; head; length++)
	{
		head = head->next;
	}

	return (length);
}

/**
 * linked_to_array - creates an array with the values of the linked list.
 * @head: pointer to the head of the linked list.
 * @size:  size of the linked list.
 *
 * Return: Pointer to array with values of linked list.
 */
int *linked_to_array(listint_t *head, int size)
{
	int *array_of_linked, *copy_array, i;

	if (head == NULL)
	{
		return (NULL);
	}
	array_of_linked = malloc(sizeof(int) * size);
	if (array_of_linked == NULL)
	{
		return (NULL);
	}
	copy_array = array_of_linked;
	for (i = 0; i < size; i++)
	{
		*copy_array = head->n;
		copy_array++;
	}
	return (array_of_linked);
}

/**
 * is_palindrome - checks if a linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: 0 if is not palindrome, 1 instead.
 */
int is_palindrome(listint_t **head)
{
	int length = 0, *array_numbers, i, j;

	if (head == NULL)
	{
		return (1);
	}
	length = length_linked_list(*head);
	if (length == 0)
	{
		return (1);
	}
	array_numbers = linked_to_array(*head, length);
	if (array_numbers == NULL)
	{
		return (0);
	}
	j = length - 1;
	for (i = 0; i < (length / 2); i++)
	{
		if (array_numbers[i] == array_numbers[j])
		{
			continue;
		}
		else
		{
			free(array_numbers);
			return (0);
		}
		j--;
	}
	free(array_numbers);
	return (1);
}
