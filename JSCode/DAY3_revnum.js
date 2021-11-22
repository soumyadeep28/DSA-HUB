//Write a program to reverse a given integer number
//The remainder of the number can be fetched and the number can be divided by 10 to remove the the digit in loop till number becomes 0
//A simple approach to reverse a number could also be to convert it in to a string and then reverse it



const num = 3849;

function reverseGivenInteger(num) {
    // write your solution here
    var rem ;
    var  sum = 0 ;
    while(num > 0)
    {
        rem = num % 10 ;
        sum = sum * 10 + rem ;
        num = Math.floor(num / 10) ;
        console.log(sum);

    }
    console.log(sum);

    return sum ;
}

console.log(`Reversed integer is: ${reverseGivenInteger(num)}`)
