//generated with matique, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[100005];
ll int dp[100005][8];
ll int y1;
ll int f(int x1,int x2){
if(dp[x1][x2]==-1){
if(x2==0){
dp[x1][x2] = f(x1,1)+f(x1+1,2);
}
else if((x2==1)&&(x1==0)){
dp[x1][x2] = (a[x1]>=0);
}
else if(x2==1){
dp[x1][x2] = (a[x1]>=0)+f(x1-1,x2);
}
else if((x2==2)&&(x1==y1)){
dp[x1][x2] = 0;
}
else{
dp[x1][x2] = (a[x1]<=0)+f(x1+1,x2);
}
}
 return dp[x1][x2];}
int main() {
cin >> y1;
for(int x1=0; x1 < 100000; x1++){
for(int x2=0; x2 < 3; x2++){
dp[x1][x2]=-1;
}
}
for(int x1=0; x1 < y1; x1++){
cin >> a[x1];
}
ll int mn = 1000000000;
for(int x1=0; x1 < y1; x1++){
for(int x2=0; x2 < 1; x2++){
mn = min(mn,f(x1,x2));
}
}
cout << mn << endl;
}