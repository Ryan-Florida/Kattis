#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::vector;

int main()
{
    int a, b, sum = 0;
    vector<int> array;

    cin >> a >> b;
    array.resize(a);


    for(int i = 0; i < b; ++i)
    {
        int j, x, y;
        cin >> j >> x >> y;
        --x;
        ++y;
        switch(j)
        {
            case 0:
                for(int k = x; k < y - 1; ++k)
                    sum += array[k]%((int)1e9 + 7);
                cout << sum << '\n';
                break;
            case 1:
                for(int k = x; k < y + 1; ++k)
                    array[k] += (k + 1)*(k + 2)*(k + 3);
                for(int z = 0; z < a; ++z)
                    cout << array[z] << ' ';
                cout << '\n';
                break;
            case 2:
                for(int z = 0; z < a; ++z)
                    cout << array[z] << ' ';
                cout << '\n';
                for(int k = x; k < y + 1; ++k)
                    array[k] -= (k + 1)*(k + 2)*(k + 3);
                for(int z = 0; z < a; ++z)
                    cout << array[z] << ' ';
                cout << '\n';
                break;
        }
    }

    return 0;
}
