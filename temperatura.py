# Cria variável e armazena a opção de conversão
opEscolhida = int(input(f'\nQual conversão deseja realizar?\n\n1 - Celsius para Fahrenheit\n2 - Celsius para Kelvin\n3 - Fahrenheit para Celsius\n4 - Fahrenheit para Kelvin\n5 - Kelvin para Celsius\n6 - Kelvin para Fahrenheit\n\nOpção: '))

# Cria variável e armazena a temperatura digitada pelo usuário
temperaturaConversao = float(input('\nDigite a temperatura a ser convertida: '))

# Cria função para realizar o cálculo, que recebe a temperatura digitada
def realizaConversao(temp):
    
    # Realiza match com a opção escolhida
    match(opEscolhida):
             
        # Caso opção tenha sido Celsius para Fahrenheit
        case 1:

            # Calcula a conversão
            temperaturaFinal = (temp * 1.8) + 32
            return f'{temperaturaFinal} °F'
            
        # Caso opção tenha sido Celsius para Kelvin 
        case 2:

            # Calcula a conversão
            temperaturaFinal = temp + 273
            return temperaturaFinal + ' K'
            
        # Caso opção tenha sido Fahrenheit para Celsius
        case 3:

            # Calcula a conversão
            temperaturaFinal = (temp - 32) / 1.8
            return temperaturaFinal + ' °C'
            
        # Caso opção tenha sido Fahrenheit para Kelvin
        case 4:

            # Calcula a conversão
            temperaturaFinal = ((temp - 32) * (5/9)) + 273
            return temperaturaFinal + ' K'
        
        # Caso opção tenha sido Kelvin para Celsius 
        case 5:

             # Calcula a conversão
            temperaturaFinal = temp - 273
            return temperaturaFinal + ' °C'
        
        # Caso opção tenha sido Kelvin para Fahrenheit  
        case 6:

            # Calcula a conversão
            temperaturaFinal = ((temp - 273) * 1.8) + 32
            return temperaturaFinal + ' °F'

# Mostra o resultado da conversão na tela
print(f'Resultado da conversão: {realizaConversao(temperaturaConversao)}')