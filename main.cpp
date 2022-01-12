#include <queue>
#include <fstream>
#include <iostream>
#include <tuple>
#include <set>
#include <map>

int w=100,h=100,fac=5;
//to go from the first part of the problem to the second requires only to change fac from 1 to 5
int** old_grid=new int*[h];
int** new_grid=new int*[fac*h];

using namespace std;

using point=pair<int,int>;
using node=pair<int,point>;

int main(){

    for(int i=0;i<h;i++){
        old_grid[i]=new int[w];
        for(int r=0;r<fac;r++)new_grid[fac*i+r]=new int[fac*w];
    }

ifstream input_str=ifstream("input");
char dig;
for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
        input_str>>dig;
        old_grid[i][j]=dig-'0';
    }
}
input_str.close();
int c;
for(int r=0;r<fac;r++){
    for(int s=0;s<fac;s++){
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                c=(old_grid[i][j]+r+s)%9;
                new_grid[r*h+i][s*w+j]=c?c:9;
            }
        }
    }
}


priority_queue<node,vector<node>,greater<node>> candidate_nodes{};
set<point>expanded_nodes{};
set<point>considered_nodes{};
map<point,int>values{};

h*=fac;
w*=fac;

candidate_nodes.push(node{0,point{0,0}});
considered_nodes.emplace(point{0,0});
values[pair<int,int>{0,0}]=0;
int cost,x,y,new_cost;
bool is_candidate;
point p,new_p;
node nd;

while(!candidate_nodes.empty()){

    nd=candidate_nodes.top();
    candidate_nodes.pop();

    cost=nd.first;
    p=nd.second;

    y=p.first;
    x=p.second;

    if((y==h-1)&&(x==w-1)){
        cout<<cost<<endl;
        return 0;
    }

    expanded_nodes.emplace(p);

    if(y<h-1){
        new_cost=cost+new_grid[y+1][x];
        new_p=point{y+1,x};
        is_candidate=expanded_nodes.find(new_p)==expanded_nodes.end();
        is_candidate&=((considered_nodes.find(new_p)==considered_nodes.end())||(values[new_p]>new_cost));

        if(is_candidate){
            candidate_nodes.push(node{new_cost,new_p});
            considered_nodes.emplace(new_p);
            values[new_p]=new_cost;
        }
    }

    if(x<w-1){
        new_cost=cost+new_grid[y][x+1];
        new_p=point{y,x+1};
        is_candidate=expanded_nodes.find(new_p)==expanded_nodes.end();
        is_candidate&=((considered_nodes.find(new_p)==considered_nodes.end())||(values[new_p]>new_cost));

        if(is_candidate){
            candidate_nodes.push(node{new_cost,new_p});
            considered_nodes.emplace(new_p);
            values[new_p]=new_cost;
        }
    }

    if(y>0){
        new_cost=cost+new_grid[y-1][x];
        new_p=point{y-1,x};
        is_candidate=expanded_nodes.find(new_p)==expanded_nodes.end();
        is_candidate&=((considered_nodes.find(new_p)==considered_nodes.end())||(values[new_p]>new_cost));

        if(is_candidate){
            candidate_nodes.push(node{new_cost,new_p});
            considered_nodes.emplace(new_p);
            values[new_p]=new_cost;
        }
    }

    if(x>0){
        new_cost=cost+new_grid[y][x-1];
        new_p=point{y,x-1};
        is_candidate=expanded_nodes.find(new_p)==expanded_nodes.end();
        is_candidate&=((considered_nodes.find(new_p)==considered_nodes.end())||(values[new_p]>new_cost));

        if(is_candidate){
            candidate_nodes.push(node{new_cost,new_p});
            considered_nodes.emplace(new_p);
            values[new_p]=new_cost;
        }
    }
}

return -1;
}

