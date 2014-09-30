#include<iostream>

using namespace std;

int main(void) {
    int c, n, x, i, j, min, max;
    while (cin >> i >> j) {
        if (i > 0 && j > 0) {
            min = 0;
            max = 0;
            if (i > j) {
                i = i + j;
                j = i - j;
                i = i - j;
            }
            for (x=i; x<=j; x++) {
                c = 1;
                n = x;
                while (n > 1) {
                    if (n%2) n = 3*n + 1;
                    else n = n/2;
                    c++;
                }
                min = c;
                if (max < min)
                    max = min;
            }
            cout << i << " " << j << " " << max << endl;
        }
    }
}