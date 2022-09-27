const { createDiffieHellmanGroup } = require("crypto");
var ps = require("prompt-sync");
var prompt = ps();
//1
/*
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
//3
/*
let ar = prompt("Give a year: ");
let monad = prompt("Give a month (first 3 letters and in swedish)")

if ((ar % 400 == 0 || ar % 4 == 0) && ar % 100 != 0){
    if (monad == "jan"){
        console.log("30")
    } else if (monad == "feb"){
        console.log("29")
    } else if (monad == "mar"){
        console.log("30")
    } else if (monad == "apr"){
        console.log("31")
    } else if (monad == "maj"){
        console.log("30")
    } else if (monad == "jun"){
        console.log("31")
    } else if (monad == "jul"){
        console.log("30")
    } else if (monad == "agu"){
        console.log("31")
    } else if (monad == "sep"){
        console.log("30")
    } else if (monad == "okt"){
        console.log("31")
    } else if (monad == "nov"){
        console.log("30")
    } else if (monad == "dec"){
        console.log("31")
    };
} else {
    if (monad == "jan"){
        console.log("30")
    } else if (monad == "feb"){
        console.log("28")
    } else if (monad == "mar"){
        console.log("30")
    } else if (monad == "apr"){
        console.log("31")
    } else if (monad == "maj"){
        console.log("30")
    } else if (monad == "jun"){
        console.log("31")
    } else if (monad == "jul"){
        console.log("30")
    } else if (monad == "agu"){
        console.log("31")
    } else if (monad == "sep"){
        console.log("30")
    } else if (monad == "okt"){
        console.log("31")
    } else if (monad == "nov"){
        console.log("30")
    } else if (monad == "dec"){
        console.log("31")
    };
};
*/

//4
/*
let num_input1 = prompt("Skriv 1 nummer: ");
let num_input2 = prompt("Skriv 1 nummer: ");
let num_input3 = prompt("Skriv 1 nummer: ");

let arr_num = []
arr_num.push(num_input1, 1);
arr_num.push(num_input2, 2);
arr_num.push(num_input3, 3);

arr_num.sort((a, b) => a - b);

console.log(arr_num[2]);
*/

//5
/*
let num_input1 = prompt("Skriv 1 nummer: ");
let num_input2 = prompt("Skriv 1 nummer: ");
let num_input3 = prompt("Skriv 1 nummer: ");

let arr_num = [];
arr_num.push(num_input1);
arr_num.push(num_input2);
arr_num.push(num_input3);

arr_num.sort((a, b) => a - b);

console.log(arr_num);
*/
//6
/*
console.log("Växande, Avtagande Eller Inget!")
let num_input1 = prompt("Skriv 1 nummer: ");
let num_input2 = prompt("Skriv 1 nummer: ");
let num_input3 = prompt("Skriv 1 nummer: ");

let arr_num = [];
arr_num.push(num_input1, 0);
arr_num.push(num_input2, 1);
arr_num.push(num_input3, 2);

if (arr_num[0] > arr_num[1] && arr_num[1] < arr_num[2]) {
    console.log("Avtagande!");
} else if (arr_num[0] < arr_num[1] && arr_num[1] > arr_num[2]) {
    console.log("Växande!");
} else{
    console.log("Inget av dem!")
}
*/
//7
/*
let tecken = prompt("Skriv ett tecken:  ");

var spec = /^[!@#$%^&*()åäöÅÄÖ_+\-=\[\]{};':"\\|,.<>\/?]*$/;
var alphabet = /^[abcdefghijklmnopqrstuvwxyz]*$/;
var alphabetU = /^[ABCDEFGHIJKLMNOPQRSTUVWXYZ]*$/;

if (tecken.match(spec)){
    console.log("SPECIAL LETTER");
} else if (tecken.match(alphabet) || tecken.match(alphabetU)){
    console.log("LETTER!");
    if (tecken.match(alphabet)){
        console.log("LOWERCASE!");
        if (tecken == "a" || tecken == "o" || tecken == "i" || tecken == "y" || tecken == "e" || tecken == "u"){
            console.log("VOKAL!");
        } else{
            console.log("KONSONANT!");
        };
    } else{
        console.log("UPPERCASE");
        if (tecken == "A" || tecken == "O" || tecken == "I" || tecken == "Y" || tecken == "E" || tecken == "U"){
            console.log("VOKAL!");
        } else{
            console.log("KONSONANT!");
        };
    };
} else if (isNaN(tecken) == false){
    console.log("DET ÄR NUMMMER MANN!");
    if (tecken % 2 == 0 || tecken == -1){
        console.log("JÄMNT");
    } else {
        console.log("OJÄMNT");
    }
} else {
    console.log("DET ÄR INGET AV DEM DU KAN INTE SKRIVA SÅDANT");
};
*/
//8
/*
let monad = prompt("Ge mig en månad(i numberform): ");
let dag = prompt("ge mig en dag (i numberform): ")
let monad_int = parseInt(monad)
let dag_int = parseInt(dag)

if (monad_int == 1){
    dag_int += 0
} else if (monad_int == 2){
    dag_int += 31
} else if (monad_int == 3){
    dag_int += 59
} else if (monad_int == 4){
    dag_int += 90
} else if (monad_int == 5){
    dag_int += 120
} else if (monad_int == 6){
    dag_int += 151
} else if (monad_int == 7){
    dag_int += 181
} else if (monad_int == 8){
    dag_int += 212
} else if (monad_int == 9){
    dag_int += 242
} else if (monad_int == 10){
    dag_int += 273
} else if (monad_int == 11){
    dag_int += 304
} else if (monad_int == 12){
    dag_int += 334
};

console.log(dag_int);

let vecka = 0;
vecka = dag_int / 7;
let vecka_math = Math.floor(vecka)

console.log(vecka_math);
*/
//9
/*
let sida1 = prompt("Ge mig en sida: ")
let sida2 = prompt("Ge mig en sida: ")
let sida3 = prompt("Ge mig en sida: ")

if ((sida1**2)+(sida2**2) == (sida3**2)){
    console.log("WOW such triangel!")
} else {
    console.log("WRONG")
};
*/
//10
/*
let kwh = prompt("How many kwh you spend:   ");

if (kwh <= 50){
    console.log(kwh *= 0.5, "kr");
} else if (kwh > 50 && kwh <= 150){
    console.log((50 * 0.5)+((kwh-50)*0.77), "kr");
} else if (kwh > 150 && kwh <= 250){
    console.log((50 * 0.5)+((100)*0.77)+((kwh-150)*1.3), "kr");
} else if (kwh > 250){
    console.log(((50 * 0.5)+((100)*0.77)+((100)*1.3)+((kwh-250)*1.7))*1.2, "kr");
};
*/