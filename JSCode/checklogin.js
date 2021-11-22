var islogged = true ;
var email = true ;
var card = false ;

// if(islogged){
//     console.log("already LOGGed in successfully");
//     if(email){
//         console.log("email is given\n");
//         if(card){
//             console.log("card details are given");
//         }
//     }
// }


if( email && islogged && card){
    console.log("you can not access the code");
}


if( email && islogged || card){
    console.log("you can access the code ");
}