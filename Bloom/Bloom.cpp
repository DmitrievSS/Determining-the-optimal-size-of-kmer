#define MAXKMER 40
#define MINKMER 40
#include <vector>
#include <string>
#include <math.h>
#include <iostream>
#include <fstream>
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
    vector< bool > list;
    vector< int > tmp;
    vector< vector<int> > hashtable;
public:
    int k;
    bloom_filter(int n, int p){
        m = -n * log(p) / (log(2)*log(2));
        k = m / n * log(2);
        list = vector<bool>(m);
        for (int i =0; i < m; i++)
            list[i] = false;

        tmp = vector<int>(k);
        for (int i = 0; i < k; i++){
            int x = i;
            hashtable.push_back(vector<int>(MAXKMER));
            hashtable[i].push_back(x + 1);
            for (int j = 1; j < MAXKMER; j++){
                hashtable[i].push_back(hashtable[i][j - 1]*(x + 1));
            }
        }
    }
    
    int hashfunc(int k, string str, int prev = -1, char c = '_'){
        int x = k;
        int res = 0;
        if (prev == -1 && c == '_'){
            for (int i = 0; i < str.size(); i++){
                res = (res + str[i] * hashtable[x - 1][i]); 
            }
        }
        if (prev != -1 && c == '_')
            res = prev + str[str.size() - 1] * hashtable[x - 1][str.size() - 1];
        if (prev != -1 && c != '_')
            res = (prev - c*x)/ x + str[str.size() - 1] * hashtable[x - 1][str.size() - 1];
        return res;
    }

    pair<bool, vector<int> > exists(string kmer, vector<int> prev = vector<int>(0), char c = '_'){
        bool result = false;
        if (prev.size() == 0){
            prev = defvect<int>(-1,k);
        }
        for (int i = 0;  i < k; i++){
            int kmer_hash = hashfunc(i, kmer,prev[i],c);
            tmp[i] = kmer_hash;
            if (!list[(m + kmer_hash) % m]){
                result = true;
            }
        }
        if (result){
            for (const auto &i : tmp){
                list[(m + i) % m] = true;
            }
        }
        return pair<bool, vector<int>>(result,tmp);
    }
}; 

vector<int> differentkmer(MAXKMER - MINKMER);
pair<bool, vector<int>> exist (vector<bloom_filter> bf, string kmer, int kstart, string line){
    pair<bool,vector <int>> kmerhashes;
    if  (kmer.size() >= 20)
        kmerhashes = bf[kmer.size() - kstart -1].exists(kmer);
    else
        kmerhashes = bf[kmer.size() - kstart -1].exists(kmer, exist(bf, kmer.substr(0,kmer.size()-1), kstart, line).second);
    if (kmerhashes.first)
        differentkmer[kmer.size() - kstart -1] ++;
    pair<bool,vector <int>> lastkmerhashes = kmerhashes;
    for (int i = 1; i < line.size() - kmer.size() + 1; i++){
        lastkmerhashes = bf[kmer.size() - kstart - 1].exists(line.substr(i,kmer.size()), lastkmerhashes.second, line[i - 1]);
        if (lastkmerhashes.first)
            differentkmer[kmer.size() - kstart - 1]++;
    }
    return kmerhashes;
}


int main(){
    vector<bloom_filter> bf;
    bf.reserve(MAXKMER - MINKMER + 1);
    for ( int i = 0; i < MAXKMER - MINKMER + 1; i++){
        bf.push_back(bloom_filter(5000, 0.01));
    }
    ifstream input("new.fastq");
    string line;
    while (getline(input, line)){
        if (line[0] == '@'){
            getline(input, line);
            line = line.substr(0, line.size()-1);
            exist(bf, line.substr(0, MAXKMER),MINKMER-1,line);
        }
    }
    input.close();
    ofstream output ("output");
    for (auto &i : differentkmer){
        cout << "different " << i+20<<"mers = " << differentkmer[i] <<"\n";
    }
    return 0;
}
