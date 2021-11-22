#include<iostream>
using namespace std;
int main()
{
    int n , sum =0 ;
    cout<<"Enter the eN number:"<<endl;
    cin>>n;

    for(int i =0 ; i<n ; i++)
    {
        sum = sum+i;
    }

    cout<<"Sum of N number"<<sum;

}