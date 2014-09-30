#include<iostream>

using namespace std;

void swap(int *i, int *j, bool condition) {
    if (condition) {
        *i = *i + *j;
        *j = *i - *j;
        *i = *i - *j;
    }
}

int problem(int n) {
    int i = 1;
    while (n > 1) {
        if (n%2) n = 3*n + 1;
        else n = n/2;
        i++;
    }
    return i;
}

int get_max_interval(int i, int j) {
    int x, min = 0, max = 0;
    swap(&i, &j, i > j);
    for (x=i; x<=j; x++) {
        min = problem(x);
        if (max < min) max = min;
    }
    return max;
}

int main(void) {
    int a, b;
    while (cin >> a >> b) {
        if (a > 0 && b > 0) {
            cout << a << " " << b << " " << get_max_interval(a,b) << endl;
        }
    }
    return 0;
}