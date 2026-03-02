const dadosOriginais = [
    {
        "mercado": "Carrefour",
        "data": "2025-01-01",
        "produtos": [
            { "nome": "Arroz", "preco": 10, "qtd": 2 },
            { "nome": "Feijao", "preco": 7, "qtd": 2 }
        ]
    },
    {
        "mercado": "Carrefour",
        "data": "2025-01-02",
        "produtos": [
            { "nome": "Arroz", "preco": 15, "qtd": 2 },
            { "nome": "Macarrao", "preco": 2, "qtd": 2 }
        ]
    },
    {
        "mercado": "Carrefour",
        "data": "2025-01-03",
        "produtos": [
            { "nome": "Feijao", "preco": 8, "qtd": 2 }
        ]
    }
];

// Mapa para organizar os dados por produto
const produtosMap = {};

for (const entrada of dadosOriginais) {
    const dataFormatada = entrada.data.split("-").reverse().join("-"); // "yyyy-mm-dd" => "dd-mm-yyyy"
    
    for (const produto of entrada.produtos) {
        const nome = produto.nome;
        if (!produtosMap[nome]) {
            produtosMap[nome] = {
                produto: nome,
                variacaoData: [],
                variacaoPreco: []
            };
        }
        produtosMap[nome].variacaoData.push(dataFormatada);
        produtosMap[nome].variacaoPreco.push(produto.preco);
    }
}

// Resultado final
const resultado = [
    {
        mercado: "Carrefour",
        dados: Object.values(produtosMap)
    }
];

console.log(resultado);