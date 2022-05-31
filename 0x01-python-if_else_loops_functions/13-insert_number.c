#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of the lisit
 * @h: pointer to the head
 * Return: number of nodes
 */
size_t print_listint_t(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;

	while (current != NULL)
	{
		print("%i\n", current->n);
		current = current->next;
		n++:
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end
 * @head: pointer to the head
 * @n: int
 * Return: address of new element or NULL if failed
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			cureent = current->next;
		current->next = new;
	}
	return (new);
}
/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list head
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
