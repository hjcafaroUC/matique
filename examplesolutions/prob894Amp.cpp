
//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[105];
ll int dp[105][8];
ll int y1;
string s;
ll int f(int x1,int x2){
if(dp[x1][x2]==-1){
if(x1>=y1){
dp[x1][x2] = 0;
}
else if((x2==0)&&(s[x1]=='Q')){
dp[x1][x2] = f(x1+1,1)+f(x1+1,0);
}
else if(x2==0){
dp[x1][x2] = f(x1+1,0);
}
else if((x2==1)&&(s[x1]=='A')){
dp[x1][x2] = f(x1+1,2)+f(x1+1,1);
}
else if(x2==1){
dp[x1][x2] = f(x1+1,1);
}
else if(s[x1]=='Q'){
dp[x1][x2] = 1+f(x1+1,2);
}
else{
dp[x1][x2] = f(x1+1,2);
}
}
 return dp[x1][x2];}
int main() {
cin >> s;
y1 =s.size();
for(int x1=0; x1 < 100; x1++){
for(int x2=0; x2 < 3; x2++){
dp[x1][x2]=-1;
}
}
cout << f(0,0) << endl;
}
