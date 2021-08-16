#include <bits/stdc++.h>
using namespace std;

double mn, target;
double f(double x){
    return (x*100.0)/(mn+x);
}
int actualPos;

double round1(double var) 
{ 
    char str[40];  
    sprintf(str, "%.2f", var); 
    sscanf(str, "%f", &var);  
  
    return var;  
} 

void solve(vector<double> &nums, double ac, int i, set<pair<double, int>> &memo){
    if(ac >= target) {mn = min(mn, ac); return;}
    if(i>=nums.size()) return;

    else if (memo.find({ac, i}) == memo.end()){
        if(i!=actualPos){
            solve(nums, ac+nums[i], i+1, memo);
            memo.insert({ac+nums[i], i+1});
        }
        solve(nums,ac,i+1, memo);
        memo.insert({ac, i+1});
    }
}


int main(){
    int n, m;
    double num;
    while(true){
        cin >> n >> m;
        if (n == 0 and m == 0) break;
        vector<double> nums;
        for(int i = 0 ; i < n ; i++){
            cin >> num;
            nums.push_back(num);
        }
        target = 50 - nums[m-1];
        if (target <= 0) cout << "100.00" << endl;
        else{
            mn = 1000;
            set<pair<double, int>> memo;
            actualPos = m-1;
            solve(nums, 0, 0, memo);
            printf("%.2lf\n",round(f(nums[m-1])*100)/100.0);
        }
    }
    
    
    return 0;
}