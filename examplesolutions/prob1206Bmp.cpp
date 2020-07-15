//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[100005];
ll int dp[100005][7];
ll int y1;
ll int f(int x1,int x2){
if(dp[x1][x2]==-1){
if((x1==0)&&(x2==0)){
dp[x1][x2] = abs(a[x1]-1);
}
else if(x1==0){
dp[x1][x2] = abs(a[x1]+1);
}
else if(x2==0){
dp[x1][x2] = min(f(x1-1,0) + abs(a[x1]-1), f(x1-1,1) + abs(a[x1]+1));
}
else{
dp[x1][x2] = min(f(x1-1,0)+abs(a[x1]+1), f(x1-1,1)+abs(a[x1]-1));
}
}
 return dp[x1][x2];}
int main() {
cin >> y1;
for(int x1=0; x1 < 100000; x1++){
for(int x2=0; x2 < 2; x2++){
dp[x1][x2]=-1;
}
}
for(int x1=0; x1 < y1; x1++){
cin >> a[x1];
}
cout << f(y1-1,0) << endl;
}
