//Write a function to truncate a string to a certain number of words
//Truncate a string to a certain number of words


const str = 'JavaScript is simple but not easy to master';
const wordLimit = 3

function truncateWithWordLimit(str, wordLimit) {
    // write your solution here
    var mylist = str.split(" ");
    var myval = mylist.slice(0 , wordLimit);
    var mystr = myval.join(" ");

    return mystr;
}

console.log(`Truncated string: ${truncateWithWordLimit(str, wordLimit)}`)
