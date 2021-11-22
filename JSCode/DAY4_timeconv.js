//Write a function which can convert the time input given in 12 hours format to 24 hours format
//The check for 'AM' and 'PM' can be verified using endsWith String method
//An extra 0 would be needed if the hours have single digit




const time = '11:8PM';

function convertTo24HrsFormat(time) {
    // write your solution here
    var padd = '0';
    if (time.endsWith("AM"))
    {
        var param = time.slice(0,-2) ;
        var arr1 = param.split(":");
        if(arr1[0].length < 2)
        {
            

        }
        if (Number(arr1[0]) == 12)
        {
            arr1[0] = '00';
        }
    }else{

        var param = time.slice(0,-2) ;
        var arr1 = param.split(":");
        var param3 = Number(arr1[0])+12 ;
        if(param3>23){
            param3 = param3 - 12 ;
        }
        arr1[0] =String(param3 ) ;

    }

    if(arr1[0].length== 1)
    {
        arr1[0] = padd.concat(arr1[0])
    }
    if(arr1[1].length== 1)
    {
        arr1[1] = padd.concat(arr1[1])
    }

    var returnval = arr1[0].concat(":") ;
    returnval = returnval.concat(arr1[1]) ;

    return returnval ;
}

console.log(`Converted time: ${convertTo24HrsFormat(time)}`)
