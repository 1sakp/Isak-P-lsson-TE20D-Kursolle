//1
var ps = require("prompt-sync");
var prompt = ps();

let input = prompt("Skriv nummer mellan 10 och 20:  ");
if (input > 20 || input < 10){
    console.log("Utanför intervall")
} else{
    console.log("innanför intervall")
};

//4
let num_input1 = prompt("Skriv 1 nummer: ");
let num_input2 = prompt("Skriv 1 nummer: ");
let num_input3 = prompt("Skriv 1 nummer: ");

let arr_num = []
arr_num.push(num_input1, 1);
arr_num.push(num_input2, 2);
arr_num.push(num_input3, 3);

arr_num.sort()

console.log(arr_num)