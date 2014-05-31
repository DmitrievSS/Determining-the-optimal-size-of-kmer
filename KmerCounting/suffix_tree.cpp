#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
using namespace std;


struct node {
    int l, r, par, link;
    map<char, int> next;
    node (int l=0, int r=0, int par=-1):l(l), r(r), par(par), link(-1){

    }
    int len(){
        return r - 1;
    }
    int &get (char c){
        if (!next.count(c)) 
            next[c] = -1;
        return next[c];
    }
};
        
class state {
public:
    int v, pos;
    state (int v, int pos) : v(v), pos(pos)  {    
    }
    state () : v(0), pos(0){
    }
};


class tree{
private:
    state ptr;
    string s;
    vector<node> t;
    int sz;
public:
    tree(string str){
        s = str;
        t = vector<node>(str.size() + 1);
        ptr = state(0, 0);
    }
    state go (state st, int l, int r) {
        while (l < r)
            if (st.pos == t[st.v].len()) {
                st = state (t[st.v].get( s[l] ), 0);
                if (st.v == -1)  return st;
            }
            else {
                if (s[ t[st.v].l + st.pos ] != s[l])
                    return state (-1, -1);
                if (r-l < t[st.v].len() - st.pos)
                    return state (st.v, st.pos + r-l);
                l += t[st.v].len() - st.pos;
                st.pos = t[st.v].len();
            }
        return st;
    }
    int split (state st) {
        if (st.pos == t[st.v].len()){
            printf("==\n");
            return st.v;
        }
        if (st.pos == 0){
            printf("0\n");
            return t[st.v].par;
        }
        node v = t[st.v];
        int id = sz++;
        t[id] = node (v.l, v.l+st.pos, v.par);
        t[v.par].get( s[v.l] ) = id;
        t[id].get( s[v.l+st.pos] ) = st.v;
        t[st.v].par = id;
        t[st.v].l += st.pos;
        return id;
    }
    
    int get_link (int v) {
        if (t[v].link != -1)  return t[v].link;
        if (t[v].par == -1)  return 0;
        int to = get_link (t[v].par);
        return t[v].link = split (go (state(to,t[to].len()), t[v].l + (t[v].par==0), t[v].r));
    }
     
    void tree_extend (int pos) {
        for(;;) {
            state nptr = go (ptr, pos, pos+1);
            if (nptr.v != -1) {
                ptr = nptr;
                return;
            }
     
            int mid = split (ptr);
            int leaf = sz++;
            t[leaf] = node (pos, s.size(), mid);
            t[mid].get( s[pos] ) = leaf;
     
            ptr.v = get_link (mid);
            ptr.pos = t[ptr.v].len();
            if (!mid)  break;
        }
    }
     
    void build_tree() {
        sz = 1;
        for (int i = 0; i < s.size(); ++i){
            tree_extend (i);
            printf("i %i\n", i);
        }
    }
};

int main(int argc, char** argv){
    if (argc != 2){
        printf("You need to set only 1 argument\n");
        return 1;
    }
    string reads;
    int fd = open(argv[1], O_RDONLY);
    int SIZE = 1024;
    char c [SIZE];
    int l;
    while ((l = read(fd, c, SIZE)) > 0){
        reads += c;
    }
    printf("length %i\n", reads.size());
    tree _tree(reads);
    _tree.build_tree(); 
    return 0;
}
