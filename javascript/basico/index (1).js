class celular {

  constructor () {

    this.cor = "prata";

  }

  ligar() {
    
    console.log("uma ligação");    
    return "ligando";    
    
  }

}

/*
let celular = function() {

  this.cor = "prata";

  this.ligar = function() {

    console.log("uma ligação");

    return "ligando";
  };

}
*/

let objeto = new celular();

console.log(objeto.cor);
console.log(objeto.ligar());