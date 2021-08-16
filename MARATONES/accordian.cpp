#include <vector>
#include <stack>
#include <string>
#include <iostream>
using namespace std;

bool matches(string a, string b){
	return a[0] == b[0] or  a[1] == b[1];
}



int main(){
	int i;
	string option;
	bool moves;
	while(true){
		vector<stack<string>> cards;
		cin >> option;
		if(option == "#") break;
		stack<string> aux;
		aux.push(option);
		cards.push_back(aux);

		//input
		for(i = 0 ; i < 51 ; i++){
			option.clear();
			cin >> option;
			stack<string> aux;
			aux.push(option);
			cards.push_back(aux);
		}


		i = 1;
		while(i < cards.size()){
			if(i >= 3 and not cards[i-3].empty() and matches(cards[i].top(), cards[i-3].top())){
				cards[i-3].push(cards[i].top());
				cards[i].pop();
				if(cards[i].empty()) cards.erase(cards.begin()+i);
				i = 0;
			}
			else if(not cards[i-1].empty() and matches(cards[i].top(), cards[i-1].top())){
				cards[i-1].push(cards[i].top());
				cards[i].pop();
				if(cards[i].empty()) cards.erase(cards.begin()+i);
				i = 0;
			}
			i++;
		}
		if(cards.size() == 1)
			cout << cards.size() << " pile remaining: ";
		else
			cout << cards.size() << " piles remaining: ";

		cout << cards[0].size();
		for(i = 1 ; i < cards.size() ; i++)
			cout << " " << cards[i].size();
		cout << endl;



	}


	return 0;
}