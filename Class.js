// Defining a class 
class Person {          

}
// Create an object of class Person
var p = new Person;
console.log(p)


var p = {lastname: 'Clinton', firstname: 'Bill'};
console.log('The person is', p);

class person {
    firstname;      // The variable is undefined
    lastname;
    age;
}

var p = new person;
console.log(p)

class Car {
    Brand = "";
    Model = "";
    Color = "";
    Engine = "";
    dateModified = 0;
}

var p = new Car;
console.log(p);

// Adding methods to a class


class dreamCar {
    Brand = 'Bmw';
    color = 'Blue';
    Engine = '';
    Model = 2021;
    display() {
        console.log("The Car Company's name is " + this.Brand + " and it was made in " + this.Model + " and the color is " + this.color);
    }   // The properties of the class are accessible in the methods of the class by prefixing them with the keyword this.
}

var myCar = new dreamCar;
myCar.Engine = "600 horsepower V8";     // This is a way to modify the value of the properties of an object
myCar.Model = 2022;
myCar.Brand = 'BMW';

console.log('My car in the upcoming future: ', myCar);
myCar.display();    // use of the display() method on the dreamCar object

// Another Example: students of a class

class jsClass {
    firstname = '';
    lastname = '';
    age = '';
    universityMajor = '';

    // class methods
    constructor (firstname, lastname, age, universityMajor) {
        this.firstname;
        this.lastname;
        this.age;
    }
    display() {
        console.log(`The sutdent's name is ${this.firstname} ${this.lastname} and he/she is ${this.age} years-old.`)
    }
}

var student1 = new jsClass;
student1.firstname = 'Farshid';
student1.lastname = 'Ahmadi';
student1.age = 20;
student1.display();

class babyName {
    firstname = '';
    lastname = '';
    dateOfBirth = '';
    ABO = '';
    // class methods
    constructor (firstname,lastname,dateOfBirth,ABO) {
        this.firstname;
        this.lastname;
        this.dateOfBirth;
        this.ABO;
    }
    display() {
        console.log(`The baby's name: ${this.firstname} ${this.lastname} and was born in ${this.dateOfBirth} and he/she 's blood group is ${this.ABO}.`);
    }
}

var Birth = new babyName ('Ashley', 'Anderson');
console.log("Variable Birth = ", Birth);
Birth.display();

// Arrays
// The easiest and fastest way to create an array is to use the bracket notation. The elements of the array are separated by a comma.

var sports = ['tennis', 'golf', 'boxing', 'basketball', 'volleyball', 'weightlifting', 'swimming', 'wrestling'];

// It is possible to create an empty array, we will be able to add elements to this array later.

var empty = [];
var Empty = new Array();

// Creating an array using new array

var Sports = new Array('football', 'badminton', 'table tennis', 'hand ball', 'surfing');
console.log(Sports);
console.log(sports);

// Accessing array elements

console.log('first Element: ' + sports[0]);
console.log('second Element: ' + sports[1]);
console.log('third Element: ', sports[2]);
console.log('fourth Element: ', sports[3]);
console.log('Last Element: ' + sports[sports.length -1]);
console.log('Last Element: ' + sports[-1]);     // It doesn't give you the last element. Be aware! 
console.log('undefined', sports[8]);    // It returns undefined
console.log('undefined', sports[-2]);   // It returns undefined

// Modifying the value of the element

console.log("Array before modification:");
console.log(Sports);
Sports[1] = 'hand ball';
Sports[3] = 'badminton';
console.log('Array after modification:');
console.log(Sports);

// Accessing array elements with a for() loop

for (var i=0; i<Sports.length; i++) {
    console.log(`${i +1}. ${Sports[i]}`);
}

// Accessing array elements using the foreach() method

sports.forEach(function(elem, i) {
    console.log("Sports[" + i + "]= ", elem);
});

// The difference between the for() loop and the forEach() method

var names = new Array('mohammad', 'reza', 'amin', 'sina', 'vahid');
names[9] = 'behzad';    // This (adding an element by index that is greater than the current number of elements) enlarges the array by creating elements initialized to the value undefined!
names[15] = 'Farshid';

for (var i=0; i<names.length; i++) {
    console.log(`${i}. name: ${names[i]}.`)
}

names.forEach(function(element, i) {
    console.log("names["+ i +"]= ", element);
});

// Using the push() method to insert an element 

var Fruits = ['Apple', 'Banana', 'Pineapple', 'Strawberries', 'peach', 'Pineapple'];
Fruits.push('Orange');
Fruits.push('Cherry');      // It automatically inserts the element at the end of the array.
Fruits.push('Pear');
Fruits.push('Grape');

console.log(Fruits);