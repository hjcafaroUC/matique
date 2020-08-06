//generated with matiquepro, Henry Cafaro 
# include <iostream>
#define ll long long
using namespace std;
ll int a[6];
ll int dp[105][105];
ll int c1;
ll int y1;
ll int f(int x1,int x2){
if(dp[x1][x2]==-1){
if(x2>=y1-x1){
dp[x1][x2] = 0;
}
else{
dp[x1][x2] = min(x1*(c1-x2),x1*(y1-x1))+f(x1+1,x2-1+min((c1-x2),(y1-x1)));
}
}
 return dp[x1][x2];}
int main() {
cin >> y1>>c1;
for(int x1=0; x1 < 100; x1++){
for(int x2=0; x2 < 100; x2++){
dp[x1][x2]=-1;
}
}
cout << f(1,0) << endl;
}