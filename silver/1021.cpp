#include <iostream>
using namespace std;
int main() {
	int N, M, S, Cur, Total;

	Cur = 1;
	Total = 0;
	cin >> N;
	cin >> M;
	int* arr = new int[M];

	for (int i = 0; i < M; i++) {
		cin >> S;
		arr[i] = S;
	}
	for (int i = 0; i < M; i++) {
		if (abs(arr[i] - Cur) < N - abs(arr[i] - Cur))
			Total = Total + abs(arr[i] - Cur);
		else
			Total = Total + N - abs(arr[i] - Cur);
		for (int j = i + 1; j < M; j++) {
			if (arr[j] > arr[i])
				arr[j] = arr[j] - 1;
		}
		N--;
		Cur = arr[i];
	}
	cout << Total << endl;
}