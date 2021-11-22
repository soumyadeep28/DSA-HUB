//Create a regular expression to validate if the given input is valid Indian mobile number or not
//Regular expression check has to have an optional +91 or 0 in the beginning, then an optional space and 10 digits
//test method of regular expression can be used to validate if the mobile number pattern matches or not


const number = '09876543210';

function validateMobile(number) {
    // write your solution here
    var phoneno = /^\+?[1-9]{2}?[ ]?[0-9]{10}$/ ;
    let result = phoneno.test(number) ; 
    //console.log(result);
    if(result == true){
        return result ;
    }else {
        var phoneno = /^[0]{1}[0-9]{10}$/ ;
        let result = phoneno.test(number) ;
        //console.log(result);
        if(result == true){
        return result ;
        }else{
            var phoneno = /^[0-9]{10}$/ ;
            let result = phoneno.test(number) ;
            return result ;
        }
    }

    
}

console.log(`is a valid Indian mobile number: ${validateMobile(number)}`)