//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[100005];
ll int dp[100005];
ll int y1;
ll int f(int x1){
if(dp[x1]==-1){
if(x1==0){
dp[x1] = 1;
}
else if(a[x1-1] < a[x1]){
dp[x1] = f(x1-1)+1;
}
else{
dp[x1] = 1;
}
}
 return dp[x1];}
int main() {
cin >> y1;
for(int x1=0; x1 < 100000; x1++){
dp[x1]=-1;
}
for(int x1=0; x1 < y1; x1++){
cin >> a[x1];
}
ll int mx = 0;
for(int x1=0; x1 < 100000; x1++){
mx = max(mx,f(x1));
}
cout << mx << endl;
}
