# -*- coding: utf-8 -*-
""" Código retirado do projeto
https://github.com/mayuresh/python-firebase-demo"""

from firebase import firebase

# Substitua esta URL pela de sua app
FIREBASE_URL = "https://softdes.firebaseio.com/"

if __name__ == '__main__':
    # Cria uma referência para a aplicação Firebase
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Lê o dado da base de dados
    result = fb.get('/', "Produtos")

    print("FB Data = %s" % result)

