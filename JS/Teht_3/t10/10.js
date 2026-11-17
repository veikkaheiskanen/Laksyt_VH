'use strict';
const form = document.getElementById('source');

form.addEventListener('submit', function (event) {
  event.preventDefault();
  const firstname = document.querySelector('input[name=firstname]').value;
  const lastname = document.querySelector('input[name=lastname]').value;
  document.getElementById('target').textContent = 'Your name is ' + firstname + ' ' + lastname;
});
