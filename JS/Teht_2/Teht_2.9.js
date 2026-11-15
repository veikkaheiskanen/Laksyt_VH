function even(numbers) {
    let evenNumbers = [];

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i]);
        }
    }

    return evenNumbers;
}

// Main program
let numbers = [2, 7, 4];

let result = even(numbers);

console.log("Original array:", numbers);
console.log("Even numbers:", result);