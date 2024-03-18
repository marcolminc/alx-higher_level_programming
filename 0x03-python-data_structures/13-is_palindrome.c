#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head node of the singly linked list
 * Return: 1 for palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *num_arr, left, right;
	size_t arr_size;
	listint_t *current;

	if (*head == NULL)
		return (1);
	current = *head;
	left = right = 0;
	arr_size = BUF_SIZE;
	num_arr = malloc(arr_size * sizeof(int));
	if (num_arr == NULL)
		return (0);
	while (current != NULL)
	{
		num_arr[right++] = current->n;
		if ((size_t)right >= arr_size)
		{
			arr_size *= 2;
			num_arr = realloc(num_arr, arr_size * sizeof(int));
			if (num_arr == NULL)
				return (0);
		}
		current = current->next;
	}
	right--;
	while (left <= right)
		if (num_arr[left++] != num_arr[right--])
		{
			free(num_arr);
			return (0);
		}
	free(num_arr);
	return (1);
}
