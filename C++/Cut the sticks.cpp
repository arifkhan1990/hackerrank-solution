#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

    int n,k,l,m;
    vector<int>v;
    cin >> n;

    for(int i = 0; i<n ;i++) {
            int u;
            cin >> u;
            v.push_back(u);
    }
    sort(v.begin(),v.end());
    while(true){
        cout << v.size() << endl;
          if(v.size() == 1) break;
        int t = v[0];
        for(int i = 0; i<v.size()  ;i++){
                v[i] -= t;
        }
        for(; v.front()==0;){
                  v.erase(v.begin()+ 0);

        }
    }

    return 0;
}

