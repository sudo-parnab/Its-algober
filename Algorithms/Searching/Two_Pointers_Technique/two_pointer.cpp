#include <iostream>
#include <vector>
#include <sstream>  // For std::istringstream
#include <algorithm>

using namespace std;

bool two_sum(vector<int>& arr, int target) {
    sort(arr.begin(), arr.end());

    auto left = arr.begin();
    auto right = arr.end() - 1;

    while (left < right) {
        int sum = *left + *right;
        if (sum == target) {
            return true;
        } else if (sum < target) {
            ++left;
        } else {
            --right;
        }
    }
    return false;
}

int main() {
    vector<int> arr;
    int target;

    cout << "Enter the numbers in the array separated by spaces:" << endl;

    string input;
    getline(cin, input);  // Read the entire line

    istringstream iss(input);  // Create a string stream from the input
    int num;

    // Extract numbers from the string stream
    while (iss >> num) {
        arr.push_back(num);
    }

    cout << "Enter the target value: ";
    cin >> target;

    if (two_sum(arr, target)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
