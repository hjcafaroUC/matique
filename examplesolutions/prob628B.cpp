//generated with matiquepro, Henry Cafaro
# include <iostream>
#define ll long long
using namespace std;
ll int a[300005];
ll int dp[300005];
ll int y1;
string s;
ll int f(int x1){
if(dp[x1]==-1){
if(x1==y1){
dp[x1] = 0;
}
else if((x1==0)&&(! ((s[x1]-'0')%4))){
dp[x1] = 1+f(x1+1);
}
else if(x1==0){
dp[x1] = f(x1+1);
}
else if(!(((s[x1]-'0')+(s[x1-1]-'0')*10)%4)){
dp[x1] = !((s[x1]-'0')%4)+x1+f(x1+1);
}
else{
dp[x1] = !((s[x1]-'0')%4)+f(x1+1);
}
}
 return dp[x1];}
int main() {
cin >> s;
y1 =s.size();
for(int x1=0; x1 < 300000; x1++){
dp[x1]=-1;
}
cout << f(0) << endl;
}
