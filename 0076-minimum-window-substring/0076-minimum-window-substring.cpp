class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.size();
        unordered_map<char,int> m;
        for(char ch: t) m[ch]++;
        int startInx = -1, length = INT_MAX;
        int i = 0, j = 0, count = 0;
        while(j < n) {
            if(m[s[j]] > 0) count++;
            m[s[j]]--;
            while(count == t.size()) {
                if(j - i + 1 < length) {
                    length = j - i + 1;
                    startInx = i;
                }
                m[s[i]]++;
                if(m[s[i]] > 0) count--;
                i++; 
            }
            j++; 
        }
        return(startInx == -1) ? "" : s.substr(startInx, length);
    }
};
