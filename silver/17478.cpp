#include <iostream>
#include <string>
using namespace std;
void recur(string i,string j,string k,string l,string m,string o,int n) {
	cout << i << endl;
	if (n == 0)
		cout << o << endl;
	else {
		cout << j << endl;
		cout << k << endl;
		cout << l << endl;
	}
	if (n != 0) {
		recur("____" + i, "____" + j, "____" + k, "____" +l, "____" +m,"____"+o, n - 1);
	}
	cout << m << endl;
}
int main() {
	int n;
	cin >> n;
	cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������." << endl;
	string i = "\"����Լ��� ������?\"";
	string j = "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.";
	string k = "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.";
	string l = "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"";
	string m = "��� �亯�Ͽ���.";
	string o = "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"";
	recur(i, j, k, l, m, o,n);
}