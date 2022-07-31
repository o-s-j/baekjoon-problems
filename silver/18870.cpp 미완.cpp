#include <iostream>
#include <string>
#include <sstream>
using namespace std;
#define MAX_SIZE = 1000000;

void merge(int list[], int left, int right, int mid) {
	int* sorted = new int[right - left + 1];
	int i, j, k, l;
	i = left;
	j = mid + 1;
	k = 0;
	while (i <= mid && j <= right) {
		if (list[i] <= list[j]) {
			sorted[k++] = list[i++];
		}
		else {
			sorted[k++] = list[j++];
		}
	}
	if (i > mid) {
		for (l = j; l <= right; l++) {
			sorted[k++] = list[l];
		}
	}
	else {
		for (l = i; l <= mid; l++) {
			sorted[k++] = list[l];
		}
	}
	for (int l = 0; l <= right; l++) {
		list[left + l] = sorted[l];
	}
}
void merge_sort(int list[], int left, int right) {
	int mid;
	if (left < right) {
		mid = (left + right) / 2;
		merge_sort(list, left, mid);
		merge_sort(list, mid + 1, right);
		merge(list, left, right, mid);
	}
}
int main() {
	int N, num = 0, a, i = 0;
	cin >> N;
	int* input = new int[N];
	int* arr = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> a;
		input[i] = a;
		arr[i] = a;
	}
	merge_sort(arr, 0, N - 1);
	for (int i = 0; i < N; i++) {
		cout << arr[i] << endl;
	}
	int* sorted = new int[N];
	sorted[0] = arr[0];
	num++;
	for (int i = 1; i < N; i++) {
		if (arr[i] != sorted[num - 1]) {
			sorted[num] = arr[i];
			num++;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < num; j++) {
			if (sorted[j] == input[i]) {
				cout << j << " ";
			}

		}
	}
	cout << endl;
}