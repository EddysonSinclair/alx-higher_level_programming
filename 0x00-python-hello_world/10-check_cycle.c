#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @head: list.
 * Return: integer.
 */
int check_cycle(listint_t *head)
{
	listint_t *tortoise;
	listint_t *hare;

	if (head == NULL)
		return (0);
	tortoise = hare = head;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);

}
