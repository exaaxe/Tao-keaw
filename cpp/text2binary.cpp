<<<<<<< HEAD
#include <iostream>
#include <bitset>
#include <string>

using namespace std;

int main() {
    string text;
    cout << "Enter text to convert to binary: ";
    getline(cin, text);

    cout << "Binary representation: ";
    for (char c : text) {
        cout << bitset<8>(c) << " ";
    }
    cout << endl;

    return 0;
=======
#include <iostream>
#include <bitset>
#include <string>

using namespace std;

int main() {
    string text;
    cout << "Enter text to convert to binary: ";
    getline(cin, text);

    cout << "Binary representation: ";
    for (char c : text) {
        cout << bitset<8>(c) << " ";
    }
    cout << endl;

    return 0;
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
}