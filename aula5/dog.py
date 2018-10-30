#planta do objeto

class Dog():
    def __init__(self):
        self.nome = 'bilu'
        self.raca = 'pitbull'
        self.idade = 1
        self.energia = 5

    def latir(self):
        print('au au au...')

    def dormir(self):
        self.energia = 5
        print('dormindo... {}'.format(self.energia))

    def andar(self):
        self.energia -= 1
        print('andando... {}'.format(self.energia))

        def __str__(self):
            return "nome: {} idade: {} raça".format(self.nome, self.idade, self.raca)




