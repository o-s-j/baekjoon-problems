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
	cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다." << endl;
	string i = "\"재귀함수가 뭔가요?\"";
	string j = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
	string k = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
	string l = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
	string m = "라고 답변하였지.";
	string o = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
	recur(i, j, k, l, m, o,n);
}