
const express = require("express");
const calculadora = require("C:\\Users\\Aleno\\PycharmProjects\\pythonProject\\jogoteca\\atividade 4\\calculadora.js");

const app = express();


app.get("/somar/:a/:b", (req, res) => {
  const { a, b } = req.params;
  const resultado = calculadora.somar(parseInt(a), parseInt(b));
  res.send(`Resultado da soma: ${resultado}`);
});


app.get("/subtrair/:a/:b", (req, res) => {
  const { a, b } = req.params;
  const resultado = calculadora.subtrair(parseInt(a), parseInt(b));
  res.send(`Resultado da subtração: ${resultado}`);
});


app.get("/multiplicar/:a/:b", (req, res) => {
  const { a, b } = req.params;
  const resultado = calculadora.multiplicar(parseInt(a), parseInt(b));
  res.send(`Resultado da multiplicação: ${resultado}`);
});


app.get("/dividir/:a/:b", (req, res) => {
  const { a, b } = req.params;
  const resultado = calculadora.dividir(parseInt(a), parseInt(b));
  res.send(`Resultado da divisão: ${resultado}`);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});