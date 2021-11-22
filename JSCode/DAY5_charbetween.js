//Write a function which accepts a string argument and returns the count of characters between the first and last character 'X'
//indexOf and lastIndexOf are the methods on String which returns the position of the given string in the input string from start and end respectively
//If the match is not found, these methods return -1

const str = 'JavaScript';

function getTheGapX(str) {
    // write your solution here
    var firstx = str.indexOf('X');
    var lastx = str.lastIndexOf('X');
    console.log(firstx);
    console.log(lastx);
    
    var diffvar = lastx - firstx ; 
    
    if (diffvar == 0){
        diffvar = lastx ;
    }
    


    return diffvar ;
}

console.log(`Gap between the X's: ${getTheGapX(str)}`)
