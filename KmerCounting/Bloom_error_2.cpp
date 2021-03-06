#define MAXKMER 40
#define MINKMER 20
#include <vector>
#include <string>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
template <typename T>
vector <T> defvect(T val, int size){
    vector <T> res;
    for (int i = 0; i < size; i++){
        res.push_back(val);
    }
    return res;
}
class bloom_filter{ 
private:
    int m;
    vector< int > list;
    vector< int > tmp;
    vector< vector<int> > hashtable;
public:
    int k;
    bloom_filter(int n, double p){
        m = -n * log(p) / (log(2)*log(2));
        k = m / n * log(2);
        //cout <<k<<" k \n";
        list = vector<int>(m);
        tmp = vector<int>(k);
        for (int i = 0; i < k; i++){
            int x = (2*i) + 1;
            hashtable.push_back(vector<int>(MAXKMER));
            hashtable[i][0] = x;
            for (int j = 1; j < MAXKMER; j++){
                hashtable[i][j] = (hashtable[i][j - 1]*(x));
            }
        }
    }
    
    int hashfunc(int k, string& str, int prev = -1, char c = '_'){
        int x = 2*(k-1) + 1;
        int res = 0;
        if (prev == -1 && c == '_'){
            for (int i = 0; i < str.size(); i++){
                res = (res + str[i] * hashtable[k - 1][str.size() - i - 1]) ; 
            }
            //cout <<str.size()<<"  "<< res << " full hash \n";
        }
        if (prev != -1 && c == '_'){
            res = (prev * x + str[str.size() - 1] * x);
            //cout <<str.size()<<"  "<< res << " childhash \n";
        }
        if (prev != -1 && c != '_'){
            res = ((prev  - c * hashtable[k - 1][str.size() - 1])*x + x*str[str.size() - 1]); 
            //cout <<str.size()<<"  "<< res <<" c*x "<<x<<" window hash \n";
        }
        return res;
    }

    pair<bool, vector<int> > exists(string& kmer, vector<int>&& prev = vector<int>(0), char c = '_'){
        int mintime = 10000000;
        bool firsttime = false;
        if (prev.size() == 0){
            prev = defvect<int>(-1,k);
        }
        //cout <<k << " k\n";
        for (int i = 1;  i < k; i++){
            int kmer_hash = hashfunc(i, kmer,prev[i],c);
            tmp[i] = kmer_hash;
            mintime = min(list[ abs(kmer_hash % m)], mintime);
            if (list[ abs(kmer_hash % m)] == 0){
                //cout <<kmer_hash<< " hash \n";
                firsttime = true;
            }
            list[abs(kmer_hash % m)]++;
        }
        return pair<bool, vector<int>>(!firsttime && (mintime == 2), tmp);
    }
}; 

vector<unsigned int> differentkmer;
vector<bloom_filter> bf;
pair<bool, vector<int> > exist (string&& kmer, int kstart, string &line){
    pair<bool,vector <int>> kmerhashes;
    if  (kmer.size() <= 20)
        kmerhashes = bf[kmer.size() - kstart -1].exists(kmer);
    else
        //cout << " recurs \n";
        kmerhashes = bf[kmer.size() - kstart -1].exists(kmer, exist(kmer.substr(0,kmer.size()-1), kstart, line).second);
    if (kmerhashes.first)
        differentkmer[kmer.size() - kstart -1] ++;
    pair<bool,vector <int>> lastkmerhashes = kmerhashes;
    string juy; 
    for (int i = 1; i < line.size() - kmer.size() + 1; i++){
        juy = line.substr(i,kmer.size());
        lastkmerhashes = bf[kmer.size() - kstart - 1].exists((juy), move(lastkmerhashes.second), line[i - 1]);
        if (lastkmerhashes.first)
            differentkmer[kmer.size() - kstart - 1]++;
    }
    return kmerhashes;
}


int main(int argc, char** argv){
    if (argc != 2){
        printf("You set %i, but you need to set 1 arg\n", argc - 1);
        return -1;
    }
    string name = argv[1];
    differentkmer.reserve(MAXKMER - MINKMER + 1); 
    bf.reserve(MAXKMER - MINKMER + 1);
    for ( int i = 0; i < MAXKMER - MINKMER + 1; i++){
        differentkmer.push_back(0);
        bf.push_back(bloom_filter(3000000, 0.01));
    }
    ifstream input(argv[1]);
    string line;
    while (getline(input, line)){
        if (line[0] == '@'){
            getline(input, line);
            exist(line.substr(0, MAXKMER), MINKMER - 1, line);
            getline(input, line);
            getline(input, line);
        }
    }
    input.close();
    ofstream output (name.substr(0, name.size() - 6) + "_e_2.output");
    for (int i = 0; i <= MINKMER; i++){
        output << "different " << i + 20 << "mers = " << differentkmer[i] << "\n";
    }
    return 0;
}
