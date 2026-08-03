#include <vector>
#include <string>
#include <cstring>   // memcpy

using namespace std;
class Solution {
public:
    /**
    encoded string is sent over to the network
    and is decoded back to original list of strings
    constraints 0 <= strs.length < 100
    0 <= strs[i].length < 200
 
     */
    string encode(vector<string>& strs) {
        string encoded_result;

        for (const string& str : strs) {
            // Get the length of current string
            int length = str.size();

            // Append the length as raw bytes 
            encoded_result.append(reinterpret_cast<const char*>(&length), sizeof(int));

            // Append the actual string content
            encoded_result.append(str);
        }

        return encoded_result;
    }

    /**
     Decodes a single string back to a list of strings.
      param s Encoded string to decode
      return Vector of decoded strings
     */
    vector<string> decode(string s) {
        vector<string> decoded_strings;
        int current_pos = 0;
        int total_length = s.size();

        while (current_pos < total_length) {
            // Read the length of the next string 
            int string_length = 0;
            memcpy(&string_length, s.data() + current_pos, sizeof(int));
            current_pos += sizeof(int);

            // Extract the string content based on the length read
            decoded_strings.push_back(s.substr(current_pos, string_length));
            current_pos += string_length;
        }

        return decoded_strings;
    }
};
 
