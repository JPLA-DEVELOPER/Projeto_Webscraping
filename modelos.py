class FundoImobiliario:
    def __init__(self, codigo, seguimento, cotacao_atual, ffo_yield, dividiend_yield, p_vp, valor_mercado, liquidez, qt_imoveis, preco_n2, aluguel_n2, cap_rate, vacancia_media):
       self.codigo = codigo
       self.seguimento = seguimento
       self.cotacao_atual = cotacao_atual
       self.ffo_yield = ffo_yield
       self.dividiend_yield = dividiend_yield
       self.p_vp = p_vp
       self.valor_mercado = valor_mercado 
       self.liquidez = liquidez
       self.qt_imoveis = qt_imoveis 
       self.preco_n2 = preco_n2
       self.aluguel_n2 = aluguel_n2
       self.cap_rate = cap_rate
       self.vacancia_media = vacancia_media



class Estrategia:
    def __init__(self, seguimento = "", cotacao_atual_minima = 0, ffo_yield_minimo = 0, dividiend_yield_minimo = 0, p_vp_minimo = 0, valor_mercado_minimo = 0, liquidez_minima = 0, qt_imoveis_minima = 0, preco_n2_minimo = 0, aluguel_n2_minimo = 0, cap_rate_minimo = 0, vacancia_media_maxima = 0):

        self.seguimento = seguimento
        self.cotacao_atual_minima = cotacao_atual_minima
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividiend_yield_minimo = dividiend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minima = liquidez_minima
        self.qt_imoveis_minima = qt_imoveis_minima
        self.preco_n2_minimo = preco_n2_minimo 
        self.aluguel_n2_minimo = aluguel_n2_minimo
        self.cap_rate_minimo = cap_rate_minimo 
        self.vacancia_media_maxima = vacancia_media_maxima

        
    def aplica_estrategia(self, fundo: FundoImobiliario):#Diz que a variável fundo é to tipo fundoImobiliário.
        if self.seguimento != "":
            if fundo.seguimento != self.seguimento:
                return False
        
        
        if fundo.cotacao_atual < self.cotacao_atual_minima \
            or fundo.ffo_yield < self.ffo_yield_minimo\
                or fundo.dividiend_yield < self.dividiend_yield_minimo\
                    or fundo.p_vp < self. p_vp_minimo\
                        or fundo.valor_mercado < self. valor_mercado_minimo\
                            or fundo.liquidez < self.liquidez_minima\
                                or fundo.qt_imoveis < self.qt_imoveis_minima\
                                    or fundo.preco_n2 < self.preco_n2_minimo\
                                        or fundo.aluguel_n2 < self.aluguel_n2_minimo\
                                            or fundo.cap_rate < self.cap_rate_minimo\
                                                or fundo.vacancia_media > self.vacancia_media_maxima:
            return False
        else:
            return True
            

