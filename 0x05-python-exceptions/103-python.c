#include <Python.h>
#include <stdio.h>
#include <float.h>
#include <math.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - Prints bytes object info
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Prints list object info
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_float - Prints float object info
 * @p: Python float object
 */
void print_python_float(PyObject *p)
{
	double val;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)p)->ob_fval;

	if (fabs(val - floor(val)) < DBL_EPSILON && fabs(val) < 1e16)
	{
		printf("  value: %.1f\n", val);
	}
	else if (fabs(val) >= 1e16 || fabs(val) <= 1e - 16)
	{
		printf("  value: %.17g\n", val);
	}
	else
	{
		printf("  value: %.16g\n", val);
	}
}
