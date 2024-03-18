#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the singly linked list
 * Return: 1 for palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int left, right, *num_arr;
	size_t arr_size;

	if (*head == NULL)
		return (1);
	current = *head;
	left = 0, right = 0, arr_size = 0, num_arr = NULL;
	while (current != NULL)
		arr_size++, current = current->next;
	num_arr = malloc(arr_size * sizeof(int));
	if (num_arr == NULL)
		return (0);
	current = *head;
	while (current != NULL)
	{
		num_arr[right++] = current->n;
		current = current->next;
	}
	right--;
	while (left <= right)
	{
		if (num_arr[left++] != num_arr[right--])
		{
			free(num_arr);
			return (0);
		}
	}
	free(num_arr);
	return (1);
}
