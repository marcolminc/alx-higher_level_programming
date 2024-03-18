#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the singly linked list
 * Return: 1 for palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int num_arr[1024], left, right;
	listint_t *current;

	if (*head == NULL)
		return 1;
	current = *head;
	left = right = 0;
	while (current != NULL)
	{
		num_arr[right++] = current -> n;
		current = current -> next;
	}
	right--;
	while (left <= right)
		if (num_arr[left++] != num_arr[right--])
			return (0);
	return (1);
}
