
# language: pt

Funcionalidade: Soma
    
    Cenario: adicao basica
        Quando somar "2" com "2"
        Então o resultado deve ser "4"

    Cenario: adicao valores
        Quando somar "-1" com "1"
        Então o resultado deve ser "0"