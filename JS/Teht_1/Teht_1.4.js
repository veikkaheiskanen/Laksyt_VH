let name = prompt("What is your name?");

let number = Math.floor(Math.random() * 4) + 1;

if (number === 1) {
    document.write(name + ", you are Gryffindor.");
} else if (number === 2) {
    document.write(name + ", you are Slytherin.");
} else if (number === 3) {
    document.write(name + ", you are Hufflepuff.");
} else {
    document.write(name + ", you are Ravenclaw.");
}