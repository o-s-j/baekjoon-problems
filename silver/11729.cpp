#include <iostream>
#include <cmath>
using namespace std;
void hanoi(char a,char b,char c,int n) {
	if (n == 1) {
		cout << a << " " << c << '\n';
	}
	else {
		hanoi(a, c, b, n - 1);
		cout << a << " " << c << '\n';
		hanoi(b, a, c, n - 1);
	}
}
int main() {
	int n;
	cin >> n;
	cout<<(int)pow(2,n)-1 << '\n';
	hanoi('1', '2', '3', n);
}