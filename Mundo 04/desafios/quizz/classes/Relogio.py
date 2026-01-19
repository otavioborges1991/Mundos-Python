class Relogio(hora=0, minuto=0, segundo=0, tipo='analogico'):
    
    def __init__(self, hora, minuto, segundo, tipo):
        if 'analogico' != tipo != 'digital':
            print('Tipo invalido, usando analogico')
            tipo = 'analogico'
        self.hora, self.minuto, self.segundo = self.recalcular(hora, minuto, segundo)
        self.tipo = tipo

    def tempo(self, funcao='mostar'):
        try:
            if funcao == 'ajustar':
                self.ajustar()
            elif funcao == "mostrar":
                self.mostar()
        except:
            print('Função invalida!')
            
    def tipo(self):
        print(self.tipo)

    def mostar(self, items='hms'):
        print(
            f'''
            {self.hora() if 'h' in items.lower() else ''}:
            {self.minuto() if 'm' in items.lower() else ''}:
            {self.segundo() if 's' in items.lower() else ''}
            ''')

    def ajustar(self, hora, minuto, segundo):

        # primeiro checar se hora, minuto e segundo são valores inteiros validos.
        
        try:
            hora = int(hora)
            minuto = int(minuto)
            segundo = int(segundo)
        except TypeError:
            print('Um ou mais valores invalidos. Devem ser apenas numeros inteiro 0-24 0-60')
            return



        self.hora, self.minuto, self.segundo = self.subtrair(hora, minuto, segundo)


    def recalcular(hora, minuto, segundo):
        """
        Ao invez de registrar um erro quando o usuário insere um valor
        invalido de horas, minutos e segundos, esta funão subtrai o tempo de um total
        para ter um valor certo, por exemplo, 30 horas resulta em 6 horas, porque se passam
        24 horas recomeçando o dia com mais 6.
        
        :param hora: Quantas horas
        :param minuto: Quantos minutos
        :param segundo: Quantos segundo
        """

        if 0 <= hora >= 24:
            while hora >= 24:
                hora -= 24
        else:
            hora = 0
    
        if 0 <= minuto >= 60:
            while minuto >= 60:
                minuto -= 60
        else:
            minuto = 0
        
        if 0 <= segundo >= 60:
            while segundo >= 60:
                segundo -= 60
        else:
            segundo = 0

        return hora, minuto, segundo
