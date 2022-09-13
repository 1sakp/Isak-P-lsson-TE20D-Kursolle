//1
var ps = require("prompt-sync");
var prompt = ps();

let input = prompt("Skriv nummer mellan 10 och 20:  ");
if (input > 20 || input < 10){
    console.log("Utanför intervall")
} else{
    console.log("innanför intervall")
};

//3