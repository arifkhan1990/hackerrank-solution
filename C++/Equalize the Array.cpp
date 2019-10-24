#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int a[101];
    int n , ans = 1,res = 0;
    cin >> n;
     for(int i = 0; i < n ;i++)
          cin >> a[i];
    sort( a,a+n );
    for(int i = 0; i < n-1 ;i++){
        if(a[i] == a[i+1]) ans++;
        else res = max(res,ans) , ans = 1;

    }
    res = max(res,ans);
    cout << n-res << endl;
    return 0;
}
