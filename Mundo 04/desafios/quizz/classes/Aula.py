class Aula(alunos=0, horário=None, sala=None, matéria=None):

    def __init__(self, alunos, horário, sala, matéria):

        self.alunos = self.set_alunos(alunos)
        self.horário = self.set_horário(horário)
        self.sala = self.set_sala(sala)
        self.matéria = self.set_matéria(matéria)
        self.estado = self.set_estado()

    # Métodos modificadores 'setters'
    def set_estado(self):
        if self.get_estado() == 'Aguardando':
            self.estado = 'Em Seção'
        else:
            self.estado = 'Aguardando'
    
    def set_horário(self, adicionar=0, subtrair=0, horário=False):
        if horário:
            self.horário = horário
        if adicionar != 0:
            self.horário += adicionar
        if subtrair != 0:
            self.horário -= subtrair

    def set_alunos(self, adicionar=0, subtrair=0, alunos=False):
        if alunos:
            self.alunos = alunos
        if adicionar != 0:
            self.alunos += adicionar
        if subtrair != 0:
            self.alunos -= subtrair

    def set_sala(self, sala):
        self.sala = sala

    def set_matéria(self, matéria):
        lista = open('../matérias.txt') # talvez fosse uma prática melhor ter este caminho em uma váriavel global em main.py
        if matéria in lista.readlines():
            self.matéria = matéria
        else:
            print('Matéria invalida')

    # metodos acessores 'getters'

    def get_estado(self):
        return self.estado
    
    def get_horário(self):
        return self.horário
    
    def get_alunos(self):
        return self.alunos

    def get_sala(self):
        return self.sala
    
    def get_matéria(self):
        return self.matéria
