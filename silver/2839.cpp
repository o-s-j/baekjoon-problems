#include <iostream>
using namespace std;
int main() {
	int num, s, j, o;
	cin >> num;
	s = num / 5;
	o = -1;
	bool found = false;
	while (s != -1) {
		j = num - (s * 5);
		if (j % 3 == 0) {
			o = s + j / 3;
			break;
		}
		else
			s--;
	}
	cout << o << endl;
}