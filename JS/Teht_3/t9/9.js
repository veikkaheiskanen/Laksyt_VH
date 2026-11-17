'use strict';
const button = document.getElementById('start');

button.addEventListener('click', function () {
  const calculation = document.getElementById('calculation').value;
  let result;

  if (calculation.includes('+')) {
    const numbers = calculation.split('+');
    result = parseInt(numbers[0]) + parseInt(numbers[1]);
  } else if (calculation.includes('-')) {
    const numbers = calculation.split('-');
    result = parseInt(numbers[0]) - parseInt(numbers[1]);
  } else if (calculation.includes('*')) {
    const numbers = calculation.split('*');
    result = parseInt(numbers[0]) * parseInt(numbers[1]);
  } else if (calculation.includes('/')) {
    const numbers = calculation.split('/');
    result = parseInt(numbers[0]) / parseInt(numbers[1]);
  } else {
    result = 'Invalid calculation';
  }

  document.getElementById('result').textContent = result;
});
