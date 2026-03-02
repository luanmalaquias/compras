dados1 = [
    {
        "mercado": "Carrefour",
        "data": "2025-01-01",
        "produtos": [
            {
                "nome": "Arroz",
                "preco": 10,
                "qtd": 2
            },
            {
                "nome": "Feijao",
                "preco": 7,
                "qtd": 2
            }
        ]
    },
    {
        "mercado": "Carrefour",
        "data": "2025-01-02",
        "produtos": [
            {
                "nome": "Arroz",
                "preco": 15,
                "qtd": 2
            },
            {
                "nome": "Macarrao",
                "preco": 2,
                "qtd": 2
            }
        ]
    },
    {
        "mercado": "Carrefour",
        "data": "2025-01-03",
        "produtos": [
            {
                "nome": "Feijao",
                "preco": 8,
                "qtd": 2
            }
        ]
    }
]

def get_mercado(mercado, dados_transformados):
    for dt in dados_transformados:
        if dt['mercado'] == mercado:
            return dt
    return None

def get_produto(produto, dt_dados):
    for p in dt_dados:
        if dt_dados['nome'] == produto:
            return dt_dados
    return None

dados_transformados = [
    {
        "mercado": "Carrefour",
        "dados": []
    }
]

for d in dados1:
    mercado = get_mercado(d['mercado'], dados_transformados)
    if mercado:
        for p in d['produtos']:
            produto = get_produto(p['nome'], mercado['dados'])
            if produto:
                pass
            else:
                pass
    else:
        dados_transformados.append({
            "mercado": d['mercado'],
            "dados": []
        })

print('Dados transformados \n\n', dados_transformados)