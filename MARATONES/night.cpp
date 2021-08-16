#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int maximum;

void solve(int time, int museum, vector<int> visited, vector<vector<int> >& travelTime, int visCnt, vector<int>& spendTime, vector<vector<int>>& solved, int config){
		if(time >= 0 and solved[time][config] == 0){
			//visits the museum
			visCnt++;
			visited[museum] = 1;
			int toVisit = 1 << (travelTime.size()-1-museum), newConfig;
			config = config ^ toVisit;
			solved[time][config] = 1;
			maximum = max(maximum, visCnt);

			vector<int> adjacentsTravelTime = travelTime[museum];
			for(int i = 0 ; i < adjacentsTravelTime.size() ; i++){
				if(not visited[i]){
					toVisit = 1 << (travelTime.size()-i-1);
					newConfig = config ^toVisit;
					solve(time-spendTime[museum]-adjacentsTravelTime[i], i, visited, travelTime, visCnt, spendTime, solved, newConfig);
				}
			}
		}
}








int main(){
	int n, i, num, j;

	while(true){
		cin >> n;
		if(n == 0) break;
		vector<int> spendTime, visited;
		for(i = 0 ; i < n ; i++){
			cin >> num;
			spendTime.push_back(num);
			visited.push_back(0);
		}
		vector<vector<int>> travelTime;
		for(i = 0 ; i < n ; i++){
			vector<int> empty;
			travelTime.push_back(empty);
			for(j = 0 ; j < n ; j++){
				cin >> num;
				travelTime[travelTime.size()-1].push_back(num);
			}
		}

		

		maximum = 0;
		for(i = 0 ; i < n ; i++){
			visited[i] = 1;
			solve(420-spendTime[i], i, visited, travelTime, 0, spendTime, solved, 0);
		}
		cout << maximum << endl;
	}


	return 0;
}