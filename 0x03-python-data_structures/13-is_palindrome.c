#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - recurs palindrome
 * @head: head list
 * Return: integer
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (auxilary_palindrome(head, *head));
}
/**
 * auauxilary_palindrome - function  to know if a number is a palindrome
 * @head: head list
 * @end: end list
 * Return: integer
 */
int auxilary_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (auxilary_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
