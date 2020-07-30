//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[205][205];
ll int dp[205][205];
ll int y1;
ll int y2;
ll int f(int x1,int x2){
if(dp[x1][x2]==-1){
if((x1==2)&&(x2==2)){
dp[x1][x2] = 0;
}
else if(x1<=1){
dp[x1][x2] = 0;
}
else if(x2<=1){
dp[x1][x2] = 0;
}
else{
dp[x1][x2] = 1+max(f(x1-2,x2+1),f(x1+1,x2-2));
}
}
 return dp[x1][x2];}
int main() {
cin >> y1 >> y2;
for(int x1=0; x1 < 200; x1++){
for(int x2=0; x2 < 200; x2++){
dp[x1][x2]=-1;
}
}
cout << f(y1+1,y2+1) << endl;
}
