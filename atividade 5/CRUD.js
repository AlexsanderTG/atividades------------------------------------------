const express = require('express');
const app = express();
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', __dirname);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname));

let estoque = [];

// (menu)
app.get('/', (req, res) => {
    res.render('index');
});

// Adicionar
app.post('/adicionar', (req, res) => {
    const { id, nome, qtd } = req.body;
    const novoProduto = { id, nome, qtd: parseInt(qtd) };
    estoque.push(novoProduto);
    res.redirect('/');
});

// Listar
app.get('/listar', (req, res) => {
    res.json(estoque);
});

// Remover
app.get('/excluir/:id', (req, res) => {
    const { id } = req.params;
    estoque = estoque.filter(produto => produto.id !== id);
    res.redirect('/');
});

// Editar
app.post('/editar/:id', (req, res) => {
    const { id } = req.params;
    const { qtd } = req.body;
    const index = estoque.findIndex(produto => produto.id === id);
    if (index !== -1) {
        estoque[index].qtd = parseInt(qtd);
        res.redirect('/');
    } else {
        res.status(404).send('Produto não encontrado.');
    }
});

// Iniciar o servidor
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
