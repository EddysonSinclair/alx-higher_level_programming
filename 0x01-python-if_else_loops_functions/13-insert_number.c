#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to a pointer to the head
 * @number: the number to be inputed
 * Return: new
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	int key;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	key = new->n;

	if (current == NULL || key < current->n)
	{
		new->next = current;
		current = new;
		return (new);
	}
	while (current->next != NULL && current->next->n < key)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
