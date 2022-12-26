from Stack import *

Plataformas = ['1 - Nintendo Switch','2 - Plastation 5','3 - Xbox series X']
Categoria = ['1 - Ação','2 - Aventura', '3 - Terror']

#jogos de Nintendo Switch
JogosAçaoN= ['1 - Animal Crossing: New Horizons','2 - Pokémon Scarlet e Violet','3 - Splatoon 3']
AnimalCro = Stack()
PokemonSeV = Stack()
Splatoon3 = Stack()
JogosAventuraN= ['1 - Super Mario Odyssey','2 - Kirby and the Forgotten Land','3 - Super Smash Bros. Ultimate']
SuperMarioOd = Stack()
Kirby = Stack()
SmashBros = Stack()
JogosTerrorN=["1 - Luigi's Mansion 3",'2 - Little Nightmares','3 - Fatal Frame']
LuigisM3 = Stack()
littleN = Stack()
FatalF = Stack()

#jogos de Plastation 5
JogosAçaoP= ['1 - Uncharted','2 - God of War', '3 - Spider-Man']
Uncharted = Stack()
GoW = Stack()
Spider = Stack()
JogosAventuraP= ['1 - Horizon Forbidden West','2 - Hollow Knight','3 - Cyberpunk 2077']
Horizon = Stack()
HollowK = Stack()
Cyberpunk = Stack()
JogosTerrorP=['1 - Silent Hill','2 - The Last of Us','3 - Dead by Daylight']
SilentHill= Stack()
TheLast = Stack()
DeadbD = Stack()

#jogos de Xbox
JogosAçaoX= ['1 - Halo  Infinite','2 - Rise of the Tomb Raider',"3 - Assassin's creed valhalla"]
Halo = Stack()
TombRaider= Stack()
assassin = Stack()
JogosAventuraX= ['1 - Far Cry 6','2 - Sonic Frontiers','3 - Elden Ring']
FarCry6 = Stack()
SonicF= Stack()
EldenR = Stack()
JogosTerrorX=['1 - Outlast','2 - Resident Evil 4', '3 - Friday the 13th: The Game']
Outlast= Stack()
REvil4 = Stack()
Friday13 = Stack()

#Alternativas de operação das pilhas
alternativa= ["1 - Inserir jogo na pilha ","2 - Remover jogo da pilha","3 - Consultar se a pilha está vazia","4 - Remover todos os elementos da pilha", "0 - Sair"]

while(True):
    for i in Plataformas:
            print(i)
    tipo= int(input("Selecione uma plataforma: "))
#Nintendo Switch                        
    if tipo == 1:
        print( "Categorias disponiveis: ")
        for j in Categoria:
            print(j)
        cat = int(input("Escolha uma categoria digitando o numero da categoria desejada: "))                   
# Ação Nintendo Switch 
        if cat == 1:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAçaoN:
             print👍
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Animal Crossing: New Horizons")
                        AnimalCro.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",AnimalCro.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",AnimalCro.isEmpty())
                    elif opção  == 4:
                        while(not AnimalCro.isEmpty()):
                            print("Itens removidos: ",AnimalCro.pop())                            
            if escolheJogo == 2:
                for i in alternativa:
                    print(i) 
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Pokémon Scarlet e Violet")
                        PokemonSeV.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",PokemonSeV.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",PokemonSeV.isEmpty())
                    elif opção  == 4:
                        while(not PokemonSeV.isEmpty()):
                            print("Itens removidos: ",PokemonSeV.pop())
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Splatoon 3")
                        Splatoon3.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)       
                    elif opção  == 2:
                        print("Jogo removido: ",Splatoon3.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Splatoon3.isEmpty())
                    elif opção  == 4:
                        while(not Splatoon3.isEmpty()):
                            print("Itens removidos: ",Splatoon3.pop())     
#Aventura Nintedo Switch     
        elif cat == 2:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAventuraN:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Super Mario Odyssey")
                        SuperMarioOd.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)        
                    elif opção  == 2:
                        print("Jogo removido: ",SuperMarioOd.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",SuperMarioOd.isEmpty())
                    elif opção  == 4:
                        while(not SuperMarioOd.isEmpty()):
                            print("Itens removidos: ",SuperMarioOd.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i) 
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Kirby and the Forgotten Land")
                        Kirby.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)        
                    elif opção  == 2:
                        print("Jogo removido: ",Kirby.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Kirby.isEmpty())
                    elif opção  == 4:
                        while(not Kirby.isEmpty()):
                            print("Itens removidos: ",Kirby.pop()) 
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Super Smash Bros. Ultimate")
                        SmashBros.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)        
                    elif opção  == 2:
                        print("Jogo removido: ",SmashBros.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",SmashBros.isEmpty())
                    elif opção  == 4:
                        while(not SmashBros.isEmpty()):
                            print("Itens removidos: ",SmashBros.pop())                     
#Terror Nintedo Switch      
        elif cat == 3:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosTerrorN:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i)
                while(True):       
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Luigi's Mansion 3")
                        Kirby.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)       
                    elif opção  == 2:
                        print("Jogo removido: ",LuigisM3.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",LuigisM3.isEmpty())
                    elif opção  == 4:
                        while(not LuigisM3.isEmpty()):
                            print("Itens removidos: ",LuigisM3.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i) 
                while(True):    
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Little Nightmares")
                        Kirby.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)         
                    elif opção  == 2:
                        print("Jogo removido: ",littleN.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",littleN.isEmpty())
                    elif opção  == 4:
                        while(not littleN.isEmpty()):
                            print("Itens removidos: ",littleN.pop())         
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):    
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Fatal Frame")
                        FatalF.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)         
                    elif opção  == 2:
                        print("Jogo removido: ",FatalF.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",FatalF.isEmpty())
                    elif opção  == 4:
                        while(not FatalF.isEmpty()):
                            print("Itens removidos: ",FatalF.pop())                 
#PS5                        
    elif tipo == 2:
        print( "Categorias disponiveis: ")
        for j in Categoria:
            print(j)   
        cat = int(input("Escolha uma categoria digitando o numero da categoria desejada: "))
#Ação PS5 
        if cat == 1:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAçaoP:
             print👍
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i)
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Uncharted")
                        Uncharted.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",Uncharted.pop())
                    elif opção  == 3:
                        print("Está vazia? ",Uncharted.isEmpty())
                    elif opção  == 4:
                        while(not Uncharted.isEmpty()):
                            print("Itens removidos: ",Uncharted.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("God of war")
                        GoW.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",GoW.pop())
                    elif opção  == 3:
                        print("Está vazia? ",GoW.isEmpty())
                    elif opção  == 4:
                        while(not GoW.isEmpty()):
                            print("Itens removidos: ",GoW.pop())  
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):    
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Spider-Man")
                        Spider.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)         
                    elif opção  == 2:
                        print("Jogo removido: ",Spider.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Spider.isEmpty())
                    elif opção  == 4:
                        while(not Spider.isEmpty()):
                            print("Itens removidos: ",Spider.pop())              
#Aventura PS5                        
        elif cat == 2:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAventuraP:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Horizon Forbidden West")
                        Horizon.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)    
                    elif opção  == 2:
                        print("Jogo removido: ",Horizon.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Horizon.isEmpty())
                    elif opção  == 4:
                        while(not Horizon.isEmpty()):
                            print("Itens removidos: ",Horizon.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i)
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Hollow Knight")
                        HollowK.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)     
                    elif opção  == 2:
                        print("Jogo removido: ",HollowK.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",HollowK.isEmpty())
                    elif opção  == 4:
                        while(not HollowK.isEmpty()):
                            print("Itens removidos: ",HollowK.pop())   
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):    
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=('Cyberpunk 2077')
                        Cyberpunk.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)         
                    elif opção  == 2:
                        print("Jogo removido: ",Cyberpunk.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Cyberpunk.isEmpty())
                    elif opção  == 4:
                        while(not Cyberpunk.isEmpty()):
                            print("Itens removidos: ",Cyberpunk.pop())                    
#Terror PS5                                     
        elif cat == 3:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosTerrorP:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Silent Hill")
                        SilentHill.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",SilentHill.pop())
                    elif opção  == 3:
                        print("Está vazia? ",SilentHill.isEmpty())
                    elif opção  == 4:
                        while(not SilentHill.isEmpty()):
                            print("Itens removidos: ",SilentHill.pop())                
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i)
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("The Last of Us")
                        TheLast.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)        
                    elif opção  == 2:
                        print("Jogo removido: ",TheLast.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",TheLast.isEmpty())
                    elif opção  == 4:
                        while(not TheLast.isEmpty()):
                            print("Itens removidos: ",TheLast.pop())   
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):    
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=('Dead by Daylight')
                        DeadbD.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)         
                    elif opção  == 2:
                        print("Jogo removido: ",DeadbD.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",DeadbD.isEmpty())
                    elif opção  == 4:
                        while(not DeadbD.isEmpty()):
                            print("Itens removidos: ",DeadbD.pop())                           
#Xbox series X    
    if tipo == 3:
        print( "Categorias disponiveis: ")
        for j in Categoria:
            print(j)
        cat = int(input("Escolha uma categoria digitando o numero da categoria desejada: "))
# Ação XBox                           
        if cat == 1:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAçaoX:
             print👍
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Halo Infinity")
                        Halo.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",Halo.pop())
                    elif opção  == 3:
                        print("Está vazia? ",Halo.isEmpty())
                    elif opção  == 4:
                        while(not Halo.isEmpty()):
                            print("Itens removidos: ",Halo.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Rise of the Tomb Raider")
                        TombRaider.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)       
                    elif opção  == 2:
                        print("Jogo removido: ",TombRaider.pop())
                    elif opção  == 3:
                        print("Está vazia? ",TombRaider.isEmpty())
                    elif opção  == 4:
                        while(not TombRaider.isEmpty()):
                            print("Itens removidos: ",TombRaider.pop())   
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Assassin's creed valhalla")
                        assassin.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)       
                    elif opção  == 2:
                        print("Jogo removido: ",assassin.pop())
                    elif opção  == 3:
                        print("Está vazia? ",assassin.isEmpty())
                    elif opção  == 4:
                        while(not assassin.isEmpty()):
                            print("Itens removidos: ",assassin.pop())                   
#Aventura XBox      
        elif cat == 2:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosAventuraX:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Far Cry 6")
                        FarCry6.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)        
                    elif opção  == 2:
                        print("Jogo removido: ",FarCry6.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",FarCry6.isEmpty())
                    elif opção  == 4:
                        while(not FarCry6.isEmpty()):
                            print("Itens removidos: ",FarCry6.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Sonic Frontiers")
                        SonicF.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)     
                    elif opção  == 2:
                        print("Jogo removido: ",SonicF.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",SonicF.isEmpty())
                    elif opção  == 4:
                        while(not SonicF.isEmpty()):
                            print("Itens removidos: ",SonicF.pop())
                    elif escolheJogo == 3:   
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Elden Ring")
                        EldenR.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)     
                    elif opção  == 2:
                        print("Jogo removido: ",EldenR.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",EldenR.isEmpty())
                    elif opção  == 4:
                        while(not EldenR.isEmpty()):
                            print("Itens removidos: ",EldenR.pop())                 
#Terror XBox       
        elif cat == 3:
            print("Jogos disponiveis nessa categoria: ")
            for y in JogosTerrorX:
             print(y)  
            escolheJogo =int(input("Escolha o jogo desejado: "))     
            if escolheJogo == 1:
                for i in alternativa:
                    print(i) 
                while(True):     
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Outlast")
                        Outlast.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)     
                    elif opção  == 2:
                        print("Jogo removido: ",Outlast.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Outlast.isEmpty())
                    elif opção  == 4:
                        while(not Outlast.isEmpty()):
                            print("Itens removidos: ",Outlast.pop())
            elif escolheJogo == 2:   
                for i in alternativa:
                    print(i)
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Resident Evil 4")
                        REvil4.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",REvil4.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",REvil4.isEmpty())
                    elif opção  == 4:
                        while(not REvil4.isEmpty()):
                            print("Itens removidos: ",REvil4.pop()) 
            elif escolheJogo == 3:   
                for i in alternativa:
                    print(i)
                while(True):      
                    opção = int(input("Digite uma opção: "))  
                    if opção == 0:
                        print("Fim de ciclo!") 
                        print(" ")
                        break
                    elif opção  == 1:
                        jogo=("Friday the 13th: The Game")
                        Friday13.push(jogo)      
                        print("Jogo inserido na pilha: ", jogo)      
                    elif opção  == 2:
                        print("Jogo removido: ",Friday13.pop())
                    elif opção  == 3:
                        print("Pilha de jogos está vazia?: ",Friday13.isEmpty())
                    elif opção  == 4:
                        while(not Friday13.isEmpty()):
                            print("Itens removidos: ",Friday13.pop())