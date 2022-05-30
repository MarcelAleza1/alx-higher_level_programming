#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t
 * @h: pointer
 * Return: number of nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;
	
	current = h;
	n = 0;
	
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current->next;
		n++;
	}
	return (n);
}
/**
 * add_nodeint - add node at the beginning
 * @head: pointer to start of the list
 * @n: integer to be included in node
 * Return: address of new element
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint -frees a listin_t
 * @head: pointer
 * Return: void
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
