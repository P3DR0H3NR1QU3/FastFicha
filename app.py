from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Promoções e pratos simulados
    promocoes = [
        {"imagem": "images/logoFastFicha.png", "descricao": "Promoção 1"},
        {"imagem": "images/IMG-20240424-WA0000.jpg", "descricao": "Promoção 2"},
        {"imagem": "images/logoFastFicha.png", "descricao": "Promoção 3"}
    ]

    pratos = [
        {"nome": "Prato 1", "preco": "R$38,00", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 2", "preco": "R$30,00", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 3", "preco": "R$12,50", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 4", "preco": "R$5,50", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 6", "preco": "R$9,50", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 7", "preco": "R$9,50", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 8", "preco": "R$9,50", "imagem": "images/IMG-20240424-WA0000.jpg"},
        {"nome": "Prato 9", "preco": "R$9,50", "imagem": "images/IMG-20240424-WA0000.jpg"}
    ]

    return render_template('pedidos_usuario.html', promocoes=promocoes, pratos=pratos)

if __name__ == '__main__':
    app.run(debug=True)
