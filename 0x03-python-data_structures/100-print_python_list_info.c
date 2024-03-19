#include <Python.h>
/**
 * print_python_list_info - Prints basic info about python lists.
 * @p: A pyobject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] SIze of the python List = %d\n", size);

	for (i < 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
