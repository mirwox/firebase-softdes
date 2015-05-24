from firebase import firebase

# Troque esta URL pela de seu próprio App Firebase
FIREBASE_URL = "https://softdes.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Pergunta algum valor para o usuário
    data = input("Digite algum dado: ")

    # Escreve dados no Firebase
    fb.put('/', "Produtos", data)

