#Script para agendar o desligamento do computador
import pyautogui as auto

tempos = {
    1:60,
    2:300,
    3:600,
    4:900,
    5:1800,
    6:3600,
    7:7200,
    8:1080
}

escolha = int(input(
""" #### AGENDAR O DESLIGAMENTO DO COMPUTADOR ####
   
    Escolha as opções:
    [1] 1 minuto
    [2] 5 minutos
    [3] 10 minutos
    [4] 15 minutos
    [5] 30 minutos
    [6] 1 Hora
    [7] 2 Horas
    [8] 3 Horas
    [9] Sair
    
Sua escolha: """))

try:
    if escolha == 9 or escolha not in tempos.keys():
        print('Você escolheu cancelar a execução do script.\nSeu computador não será desligado.')      
    else:
        auto.sleep(2)
        auto.hotkey('win','r')
        
        auto.sleep(2)
        auto.typewrite('cmd')
        
        auto.sleep(2)
        auto.press('enter')
        
        auto.sleep(4)
        auto.typewrite(f'shutdown -s -f -t {tempos[escolha]}')
        
        auto.sleep(2)
        auto.press('enter')
except:
    print('Você escolheu cancelar a execução do script\nSeu computador não será desligado')