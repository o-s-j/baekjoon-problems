#include <iostream>
using namespace std;
int main() {
	int fibo[41];
	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2; i < 41; i++) {
		fibo[i] = fibo[i - 1] + fibo[i - 2];
	}
	int a, b;
	cin >> a;
	int* arr = new int[a];
	for (int i = 0; i < a; i++) {
		cin >> b;
		arr[i] = b;
	}
	for (int i = 0; i < a; i++) {
		if (arr[i] == 0)
			cout << 1 << " " << 0 << endl;
		else if (arr[i] == 1)
			cout << 0 << " " << 1 << endl;
		else
			cout << fibo[arr[i] - 1] << " " << fibo[arr[i]] << endl;
	}
}