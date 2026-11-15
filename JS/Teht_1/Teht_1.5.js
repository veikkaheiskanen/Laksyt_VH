 let dice = Number(prompt("Enter the number of dice:"));
    let target = Number(prompt("Enter the sum of the eyes:"));

    let simulations = 10000;
    let successes = 0;

    for (let i = 0; i < simulations; i++) {
        let sum = 0;

        for (let j = 0; j < dice; j++) {
            sum += Math.floor(Math.random() * 6) + 1;
        }

        if (sum === target) {
            successes++;
        }
    }

    let probability = (successes / simulations) * 100;

    document.write(
        "Probability to get sum " + target + " with " + dice +
        " dice is " + probability.toFixed(2) + "%"
    );
