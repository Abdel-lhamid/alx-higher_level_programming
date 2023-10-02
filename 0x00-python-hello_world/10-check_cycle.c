#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;          /* Move one step at a time */
		fast = fast->next->next;    /* Move two steps at a time */

		/* If there is a cycle, they will meet at some point */
		if (slow == fast)
			return (1);
	}

	return (0); /* No cycle found */
}

