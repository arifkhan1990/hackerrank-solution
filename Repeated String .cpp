#include<bits/stdc++.h>
using namespace std;

int main()
{
    string a;
    long n,t , c = 0;
    int d ;
    cin >> a >> n;
    t = n/a.size();
    d = n%a.size();
     for(int i = 0; i<a.size() ;i++)
         if(a[i] == 'a') c++;
      c *= t;
     for(int i = 0 ; i<d ;i++) if(a[i] == 'a') c++;

    cout << c << endl;

    return 0;
}


