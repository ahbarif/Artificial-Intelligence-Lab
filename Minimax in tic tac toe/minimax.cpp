#include <bits/stdc++.h>
using namespace std;

void printBoard(vector<string> vec){
    cout<<"\n__Board now__:"<<endl;
    for(auto it:vec) cout<<it<<endl;
}

bool is_Winning(char sign, vector<string> vec){

    for(int i = 0; i<3; i++){
        if(vec[i][0] == sign && vec[i][1] == sign && vec[i][2] == sign) return true;
    }

     for(int i = 0; i<3; i++){
        if(vec[0][i] == sign && vec[1][i] == sign && vec[2][i] == sign) return true;
    }

    if(vec[0][0] == sign && vec[1][1] == sign && vec[2][2] == sign) return true;
    if(vec[0][2] == sign && vec[1][1] == sign && vec[2][0] == sign) return true;

    return false;
}

int find_utility(vector<string> vec){
    if(is_Winning('x', vec)) return 100;
    else if(is_Winning('o', vec)) return -100;
    else return 0;
}


int minimax(int depth, bool isMax, vector<string> vec){

    int score = find_utility(vec);

    if(score != 0) return score;

    if(depth > 9) return 0;

    if(isMax == true){
        int optimalScore = -1000;

        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                if(vec[i][j]=='-'){
                    vec[i][j] = 'x';
                    int k = minimax(depth+1, false, vec);
                    optimalScore = max(optimalScore, k);
                    vec[i][j] = '-';
                }
            }
        }

        return optimalScore;

    }

    else{

        int optimalScore = 1000;

        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                if(vec[i][j]=='-'){
                    vec[i][j] = 'o';
                    int k = minimax(depth+1, true, vec);
                    vec[i][j] = '-';
                    optimalScore = min(optimalScore, k);
                }
            }
        }

        return optimalScore;
    }

}

pair<int, int> find_best_Move(vector<string> grid, int depth){

    pair<int, int> turn = make_pair(-1, -1);

    int best = 1000;

    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){

            if(grid[i][j] == '-'){
                grid[i][j] = 'o';
                int k = minimax(depth+1, true, grid);
                grid[i][j] = '-';

                if(k < best){
                    turn = make_pair(i, j);
                    best = k;
                }
            }
        }
    }

    return turn;
}


int main()
{

    bool isResult = false;

    vector<string> grid;

    grid.push_back("---");
    grid.push_back("---");
    grid.push_back("---");

    int d = 1;

    printBoard(grid);

    cout<<"Enter row(0-2) and column(0-2):"<<endl;

    while(d<=9){


        int row, col;

        while(cin>>row>>col){
            if(grid[row][col] != '-') cout<<"Invalid move"<<endl;
            else break;
        }

        grid[row][col] = 'x';
        printBoard(grid);

        if(is_Winning('x', grid)) {
            printBoard(grid);
            cout<<"Player wins"<<endl;
            isResult = true;
            break;
        }

        d++;

        if(d>9) break;

        pair<int, int> turn = find_best_Move(grid, d);

        int rx = turn.first;
        int rc = turn.second;


   //     cout<<"r = "<<rx<<" "<<rc<<endl;

        grid[rx][rc] = 'o';

        printBoard(grid);

        d += 1;

        if(is_Winning('o', grid)) {

            cout<<"Computer wins"<<endl;
            isResult = true;
            break;
        }

    }

    if(isResult == false) cout<<"Game draw"<<endl;

    return 0;

}




