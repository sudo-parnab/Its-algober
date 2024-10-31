#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int binarySearch(const vector<int>& arr, int l, int r, int x);
int exponentialSearch(vector<int>& arr, int n, int x) {
    sort(arr.begin(), arr.end());

    if (arr[0] == x)
        return 0;

    int i = 1;
    while (i < n && arr[i] <= x)
        i *= 2;

    return binarySearch(arr, i / 2, min(i, n - 1), x);
}

int binarySearch(const vector<int>& arr, int l, int r, int x) {
    if (r >= l) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == x)
            return mid;

        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);

        return binarySearch(arr, mid + 1, r, x);
    }

    return -1;
}

int main() {
    vector<int> arr;
    int x;

    cout << "Enter sorted elements separated by spaces (press Enter to end input): ";

    string line;
    getline(cin, line);
    istringstream stream(line);
    int num;
    while (stream >> num) {
        arr.push_back(num);
    }

    cout << "Enter the target value to search for: ";
    cin >> x;

    int result = exponentialSearch(arr, arr.size(), x);
    if (result == -1)
        cout << "Element is not present in the array" << endl;
    else
        cout << "Element is present at index " << result << endl;

    return 0;
}
