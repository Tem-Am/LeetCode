#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;

class RandomizedSet {
private:
    unordered_map<int, int> valToIndex;
    vector<int> values;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if(valToIndex.count(val)){
            return false;
        }
        values.push_back(val);
        valToIndex[val] = values.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if(!valToIndex.count(val)){
            return false;
        }
        int index = valToIndex[val]; // get the index of remove num
        int last = values.back(); // get the last item or top item from the vector

        values[index] = last; // change wanted in index number to toppest item
        valToIndex[last] = index; // top one will ne wanted removed num

        values.pop_back();
        valToIndex.erase(val);

        return true;
    }
    
    int getRandom() {
        if(values.size() != 0){
            int randIndex = rand() % values.size();
            return values[randIndex];
        }
        else{
            return 0;
        }
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */