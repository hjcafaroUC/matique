//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[66];
ll int dp[66];
ll int y1;
ll int f(int x1){
if(dp[x1]==-1){
if(x1==0){
dp[x1] = 1;
}
else if((x1%2)==1){
dp[x1] = 0;
}
else{
dp[x1] = 2*f(x1-2);
}
}
 return dp[x1];}
int main() {
cin >> y1;
for(int x1=0; x1 < 61; x1++){
dp[x1]=-1;
}
cout << f(y1) << endl;
}
