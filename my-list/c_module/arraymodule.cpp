#ifdef _MSC_VER
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

namespace cpp {
int *array_new(size_t len) {
	return new int[len];
}

void array_delete(int *arr) {
	delete[] arr;
}

int array_get_value(int *arr, size_t index) {
	return *(arr + index);
}

void array_set_value(int *arr, size_t index, int value) {
	*(arr + index) = value;
}

}

extern "C" {
DLL_EXPORT int *array_new(size_t len) {
	return cpp::array_new(len);
}

DLL_EXPORT void array_delete(int *arr) {
	return cpp::array_delete(arr);
}

DLL_EXPORT int array_get_value(int *arr, size_t index) {
  return cpp::array_get_value(arr, index);
}

DLL_EXPORT void array_set_value(int *arr, size_t index, int value) {
  return cpp::array_set_value(arr, index, value);
}

}
