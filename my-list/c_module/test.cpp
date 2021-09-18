#include "stdio.h"
#include "arraymodule.cpp"

int main() {
	int l = 10;
	int *a = array_new(l);
	for (int i = 0; i < l; i++) {
		array_set_value(a, i, i * i);
	}
	for (int i = 0; i < l; i++) {
		printf("%d%c", array_get_value(a, i), i + 1 == l ? '\n' : ' ');
	}
}