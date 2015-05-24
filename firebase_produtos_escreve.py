import json





# Cada item vai ser um dicionário
phone = {}
phone["nome"] = "Phone 6 Gigante"
phone["codigo"] = "CM1287BRZ"
phone["preço"] = 5000.00

doce = {"nome":"Kit Kat Nestlé", "codigo": "kt0001", "preço": 3.00}
placa = {"nome": "ESP8266", "codigo": "ESP0001", "preço": 30.00 }

# Uma lista de produtos
produtos = []
produtos.append(phone)
produtos.append(doce)
produtos.append(placa)



from firebase import firebase

# Troque esta URL pela de seu próprio App Firebase
FIREBASE_URL = "https://softdes.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Converte os dados para o formato Json
    json_produtos = json.dumps(produtos)
    # Escreve dados no Firebase
    fb.put('/', "Produtos", json_produtos)


