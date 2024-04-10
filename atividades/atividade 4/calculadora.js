const somar = (a, b) => a + b;
const subtrair = (a, b) => a - b;
const multiplicar = (a, b) => a * b;
const dividir = (a, b) => (b !== 0 ? a / b : "Erro: divisão por zero");

module.exports = { somar, subtrair, multiplicar, dividir };