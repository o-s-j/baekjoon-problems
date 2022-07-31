#include <iostream>
#include <cmath>
#define swap(x,y,temp)((temp)=(x),(x)=(y),(y)=(temp))
using namespace std;
int partition(int list[], int left, int right) {
    int pivot, temp;
    int low, high;

    low = left;
    high = right + 1;
    pivot = list[left];

    do {
        do {
            low++;
        } while (low <= right && list[low] < pivot);
        do {
            high--;
        } while (high >= left && list[high] > pivot);
        if (low < high) {
            swap(list[low], list[high], temp);
        }
    } while (low < high);
    swap(list[left], list[high], temp);

    return high;
}
void quick_sort(int list[], int left, int right) {
    if (left < right) {
        int q = partition(list, left, right);
        quick_sort(list, left, q - 1);
        quick_sort(list, q + 1, right);
    }

}
int main() {
    int N,num,sum=0,many_num=0,second=0,max=0,ans=0;
    cin >> N;
    int* arr = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> num;
        arr[i] = num;
        sum = sum + num;
    }
    quick_sort(arr, 0, N - 1);
    if (round(float(sum) / N) == 0)
        cout << 0 << endl;
    else
        cout << round(float(sum) / N) << endl;
    cout << arr[int(N / 2)] << endl;
    if (N == 1)
        ans = arr[0];
    else {
        for (int i = 0; i < N - 1; i++) {
            while (arr[i] == arr[i + 1] && i < N - 1) {
                many_num++;
                i++;
            }
            if (max < many_num) {
                max = many_num;
                ans = arr[i];
                second = 1;
            }
            else if (max == many_num) {
                if (second < 2) {
                    ans = arr[i];
                    second++;
                }
            }
            many_num = 0;
        }
    }
    cout << ans << endl;
    cout << arr[N - 1] - arr[0];
}