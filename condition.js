// writing instructions

var a = 112;
var b = 56;

if (a == 12 || b > 50) {
    console.log("Condition a=12 OR b>50 is True.");
}
else console.log('Condition a=12 OR b>50 is False.');

if (a == 13 && b > 50) {
    console.log('Condition a=13 AND b>50 is True.')
}
else console.log('Condition a=13 AND b>50 is False.')

/*
In an OR condition, it suffices that one of the conditions is true for the final
condition to be true.
In an AND condition, all the conditions must be true for the final condition
to be true.
*/

if (a == 13 && b > 50) {
    console.log('Condition a=13 AND b>50 is True.');
}
else {
    if (a != 13) console.log(`a is ${a} and condition a=13 is False.`);
    else console.log('b is lesser than 50.');
}

// Loops while() and for() loops:
// Displaying numbers between 0 to 5:

var i = 0;
while (i <= 7) {
    console.log(`i = ${i}`);
    i ++;
}
/* 
As long as the condition is true, the statement (or block) is executed.
It stops when the condition becomes false.
*/

for (var x = 0; x <=5; x++) console.log(`x = ${x}`);   

/*
The for loops has three parts, seperated by ;.
the first one here is the declaration of the variable x initialized to 0 (which is the beginning of the loop.)
the second corresponds to the condition.
the third one corresponds to an instruction executed after each pass through the loop.
*/


// Definition an Calling Functions
// A function is used to give a name to a block of instructions so that it can be used in different places in the program.

// Display first 10 integers with a function

function show10FirstIntegers() {
    for (var a = 0; a <= 10; a++) console.log(`a = ${a}`);
}

// After we defined the function, we need to call it in case we want to use it.

show10FirstIntegers();

// function calculation the sum of the first 10 integers

function sumOfNumbers() {
    var total=0;    // It is a local variable 
    for (var i=0; i<=10; i++) total+=i;
    return total;
}

console.log(`The sum of first 10 integers is: ${sumOfNumbers()}`);

// function calculation the sum of numbers between two give words

var num1 = Number(prompt("Enter a number: "))
var num2 = Number(prompt("Enter a number: "))

function sumBetweenTwoNumbers() {
var total=0;
for (var i=num1; i<=num2; i++) total+=i;
return total;    
}

console.log(`the sum of the numbers between ${num1} and ${num2} is ${sumBetweenTwoNumbers()}`);