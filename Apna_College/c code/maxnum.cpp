#include<iostream>
using namespace std;

int main(){

    cout<<"enter three number";
    int a,b,c ;
    cin>>a>>b>>c;

    if(a>b){
        if(a>c)
        {
            cout<<"max value"<<a<<endl;
        }
        else{
            cout<<"max value"<<c<<endl;
        }
    }else{
        if(b>c)
        {
            cout<<"max value"<<b<<endl;
        }
        else{
            cout<<"max value"<<c<<endl;
        }
    }


    return 0;
}