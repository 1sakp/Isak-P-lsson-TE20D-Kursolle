var ps = require("prompt-sync");
var prompt = ps();
//1
/*
let num = prompt("Num:  ");
for (let i = 0; i < num; i++) {
    console.log(i+1);
};
*/
//2
/*
let num = prompt("Num:  ");
for (let i = 0; i < num; i++) {
    console.log("#####");
};
*/
//3
/*
let num = prompt("Num:  ");
let num_loop = num
while (num_loop > 0) {
    for (let i = num_loop; i > 0; i--) {
        console.log(i)
    };
    num_loop-=1
};
*/
//4
/*
let string = prompt("paledrome:    ");
function palindrome(str) {
    var re = /[^A-Za-z0-9]/g;
    str = str.toLowerCase().replace(re, '');
    var len = str.length;
    for (var i = 0; i < len/2; i++) {
      if (str[i] !== str[len - 1 - i]) {
          return false;
      }
    }
    return true;
   }
   palindrome("A man, a plan, a canal. Panama");
console.log(palindrome(string));
*/
//5
/*
let str = prompt("Num:    ");
function prime(input){
    var factors = [];
    var numStorage = input
    x=2
    while (numStorage != 1){
        var result = numStorage%x;
        if (result === 0) {
            factors.push(x);
            numStorage = numStorage/x
            x=2
        }
        else {
            x = x+1
        }
    }
    return factors.pop();
}
console.log(prime(str))
*/