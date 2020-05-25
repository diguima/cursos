/*

//***************************************************** Ouvindo eventos
window.addEventListener('focus', event => {

  console.log("focus");

});

document.addEventListener('click', event => {

  console.log("click");

});

//***************************************************** Data

let agora = new Date();

console.log(agora.toLocaleDateString('pt-br'));

*/

//***************************************************** Array

let carros = ["palio 98", "toro", "uno", 10, true, new Date(), function(){}];

carros.forEach(function(value, index) {
  console.log(index, value);
});