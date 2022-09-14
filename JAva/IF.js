//1
/*
var ps = require("prompt-sync");
var prompt = ps();

let input = prompt("Skriv nummer mellan 10 och 20:  ");
if (input > 20 || input < 10){
    console.log("Utanför intervall")
} else{
    console.log("innanför intervall")
};
*/

//2
/*
let ar = prompt("Give a year: ");

if ((ar % 400 == 0 || ar % 4 == 0) && ar % 100 != 0){
    console.log("Det är ett skottår");
} else {
    console.log("Det är inte ett skåtår")
}
*/

//4
let num_input1 = prompt("Skriv 1 nummer: ");
let num_input2 = prompt("Skriv 1 nummer: ");
let num_input3 = prompt("Skriv 1 nummer: ");

let arr_num = []
arr_num.push(num_input1, 1);
arr_num.push(num_input2, 2);
arr_num.push(num_input3, 3);


console.log(arr_num[1]);

numArray.sort(function(a, b) {if( a === Infinity ) return 1; else if( isNaN(a)) return -1;
    else return a - b;
});

console.log(arr_num);
