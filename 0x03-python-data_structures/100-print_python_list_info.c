#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int i, size_l;
	PyListObject *list;
	PyObject *item;

	size_l = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PulistObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size_l; i++ )
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i,Py_TYPE(item)->tp_name)
	}
}
