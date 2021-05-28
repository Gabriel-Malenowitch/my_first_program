import pygame
from random import randint
import time


pygame.init()

decisão = 0

janela = pygame.display.set_mode((388,500))
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
fundo1 = pygame.image.load('fundo.png')
fundo0 = pygame.image.load('fundo1.png')
fundo2 = pygame.image.load('fundo2.png')
laranja = pygame.image.load('laranja.png')
policia = pygame.image.load('policia.png')
policia1 = pygame.image.load('policia.png')
verde = pygame.image.load('verde.png')
vermelho = pygame.image.load('vermelho.png')
policiaarmada = pygame.image.load('Policia Armada.png')
policiaaberta = pygame.image.load('policia_porta_aberta.png')
explosao = pygame.image.load('explosao.png')
atropelado = pygame.image.load('atropelado.png')
text = pygame.image.load('text.png')
for i in range(0,1):
    missil1 = pygame.image.load('missil1.png')
    missil2 = pygame.image.load('missil2.png')
    missil1b = pygame.image.load('missil1b.png')
    missil2b = pygame.image.load('missil2b.png')
    missil1e = pygame.image.load('missil1e.png')
    missil2e = pygame.image.load('missil2e.png')
    missil1d = pygame.image.load('missil1d.png')
    missil2d = pygame.image.load('missil2d.png')

perdeu = False

velocidade_vermelho = 5
velocidade_laranja = 5
velocidade_verde = 5

carro_vermelho = 0
carro2 = 0
porta = 1

def mensagem_na_tela(tela,mensagem):
    import pygame
    pygame.font.init()
    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    text = fonte_perdeu.render(mensagem, 1, (0,0,0))
    tela.blit(text,(90,120))

comandos = pygame.key.get_pressed()  

#CORES
white = (255,255,255)
black = (0,0,0)
gray = (50,50,50)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
#####################

x = 161
y = 150
velocidade = 10


pos_x = 68
pos_y = 1620

larx = 161
lary = 2000

verx = 254
very = 2100

obj1 = (x, x + 69, y, y + 140) #Localização do objeto(policia)
obj2 = (pos_x, pos_x + 70, pos_y, pos_y + 150) #Localização do carro vermelho

colisao = 0
eua = 0
arma = 0

font_padrao = pygame.font.get_default_font()

stick = 0

vermelho_fora = False
laranja_fora = False
verde_fora = False

posicao = 1

for i in range(0,1):
     bl = pygame.image.load('bl.png')
     bp = pygame.image.load('bp.png')
     br = pygame.image.load('br.png')
     bt = pygame.image.load('bt.png')
     dl = pygame.image.load('dl.png')
     dp = pygame.image.load('dp.png')
     dr = pygame.image.load('dr.png')
     dt = pygame.image.load('dt.png')
     el = pygame.image.load('el.png')
     ep = pygame.image.load('ep.png')
     er = pygame.image.load('er.png')
     et = pygame.image.load('et.png')
     fl = pygame.image.load('fl.png')
     fp = pygame.image.load('fp.png')
     fr = pygame.image.load('fr.png')
     ft = pygame.image.load('ft.png')


dois_no_jogo = False
um_no_jogo = False

pygame.display.set_caption('Corrida mortal')

fundao = 0
andando = True
freio = False
fora_do_carro = False
mostrar_carro = False
velobon = 4

fundo = fundo0
eua0 = 0

tiro_alto = False
tiro_baixo = False
tiro_esquerda = False
tiro_direita = False
alvo = True
cont = 0
velocidade_missil = 20
stop = False

vermelho_explodiu = False
cve = 0
verde_explodiu = False
cvee = 0
laranja_explodiu = False
cle = 0
janela_ativa = True

cv = 0
cl = 0
cvv = 0

while janela_ativa:

    if perdeu == True:
        fundo.blit(text,(0,0))
        time.sleep(2)
        break

    janela.blit(fundo,(0,0))

    relogio = pygame.time.Clock()
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_ativa = False
    
        plit = 1
        
    if eua == 0 and eua0 == 0:
        comandos = pygame.key.get_pressed()        
        
        if comandos[pygame.K_DOWN]:
            if x + 69 >= pos_x and pos_x + 70 >= x and y + 140 >= pos_y and pos_y + 150 >= y:
                if y + 140 >= pos_y:
                    y = pos_y - 140
            if x + 69 >= larx and larx + 72 >= x and y + 140 >= lary and lary + 159 >= y:
                if y + 140 >= lary:
                    y = lary - 154
            if x + 69 >= verx and verx + 71 >= x and y + 140 >= very and very + 151 >= y:
                if y + 140 >= very:
                    y = very - 147
            else:
                y += velocidade    
        if comandos[pygame.K_LEFT]:
            if velocidade_vermelho == 0:
                plit = 1
            else: 
                x -= velocidade
            if x + 69 >= pos_x and pos_x + 70 >= x and y + 140 >= pos_y and pos_y + 150 >= y:
                if x <= pos_x + 70:
                    x = pos_x + 71
            if x + 69 >= larx and larx + 72 >= x and y + 140 >= lary and lary + 159 >= y:
                if x <= larx + 72:
                    x = larx + 73
            if x + 69 >= verx and verx + 71 >= x and y + 140 >= very and very + 151 >= y:
                if x <= verx + 71:
                    x = verx + 72
        if comandos[pygame.K_RIGHT]:
            if velocidade_vermelho == 0:
                plit = 1
            else: 
                x += velocidade
            if x + 69 >= pos_x and pos_x + 70 >= x and y + 140 >= pos_y and pos_y + 150 >= y:
                if x + 69 >= pos_x:
                    x = pos_x - 70
            if x + 69 >= larx and larx + 72 >= x and y + 140 >= lary and lary + 159 >= y:
                if x + 69 >= larx:
                    x = larx - 70
            if x + 69 >= verx and verx + 71 >= x and y + 140 >= very and very + 151 >= y:
                if x + 69 >= verx:
                    x = verx - 70

    if eua == 0:
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:  
            plit = 0

            if x + 69 >= pos_x and pos_x + 70 >= x and y + 140 >= pos_y and pos_y + 150 >= y:
                if y >= pos_y + 145 and y > pos_y + 80:
                    y = pos_y + 146
                else:
                    y -= velocidade
            if x + 69 >= larx and larx + 72 >= x and y + 140 >= lary and lary + 159 >= y:
                if y >= lary + 154 and y > lary + 92:
                    y = lary + 154
                else:
                    y -= velocidade
            if x + 69 >= verx and verx + 71 >= x and y + 140 >= very and very + 151 >= y:
                if y >= very + 146 and y > very + 80:
                    y = very + 147
                else:
                    y -= velocidade
                       
            else:
                y -= velocidade 
                eua = 0
                eua0 = 0       
        if comandos[pygame.K_LSHIFT]:
            velocidade += 1
        if comandos[pygame.K_LCTRL]:
            velocidade -= 1
        if comandos[pygame.K_x]:
            if arma == 0:
                policia = policiaarmada
                arma = 1
            else:
                policia = policia1
                arma = 0 
    
    if plit == 1:
        colisao = 0
        if x + 69 >= pos_x and pos_x + 70 >= x and y + 140 >= pos_y and pos_y + 150 >= y:
            eua = 1
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_UP]:
                eua = 0
            if y <= 0 and fora_do_carro == False:
                y = 0
                velocidade_vermelho = 0
                perdeu = True
                
                
            else:
                if y + 140 >= pos_y and y < pos_y + 30:
                    y = pos_y - 144
                    colisao = 1
                    if fora_do_carro == True:
                        vermelho_fora = True
        if x + 69 >= larx and larx + 72 >= x and y + 140 >= lary and lary + 159 >= y:
            eua = 1
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_UP]:
                eua = 0
            if y <= 0 and fora_do_carro == False:
                y = 0
                velocidade_laranja = 0
                perdeu = True
                
            else:
                if y + 140 >= lary and y < lary + 30:
                    y = lary - 144
                    colisao = 1
                    if fora_do_carro == True:
                        laranja_fora = True
        if x + 69 >= verx and verx + 71 >= x and y + 140 >= very and very + 151 >= y:
            eua = 1
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_UP]:
                eua = 0
            if y <= 0 and fora_do_carro == False:
                y = 0
                velocidade_verde = 0
                perdeu = True
                
            else:
                if y + 140 >= very and y < very + 30:
                    y = very - 145
                    colisao = 1                    
                if fora_do_carro == True:
                    verde_fora = True

    if arma == 1:
        
        if x + 37 >= pos_x and pos_x + 70 >= x + 28 and y + 184 >= pos_y and pos_y + 150 >= y:
            velocidade_vermelho = -2
            vermelho_fora = True
            eua = 0
        if x + 37 >= larx and larx + 72 >= x + 28 and y + 184 >= lary and lary + 159 >= y:
            velocidade_laranja = -2
            laranja_fora = True
            eua = 0
        if x + 37 >= verx and verx + 71 >= x + 28 and y + 184 >= very and very + 151 >= y:
            velocidade_verde = -2
            verde_fora = True
            eua = 0

    if vermelho_fora == False:

        if pos_y < -170:
            pos_y = 668
            carro_vermelho = randint(1,3)
            if carro_vermelho == 1:
                pos_x = 68
                
            elif carro_vermelho == 2:
                pos_x = 161
                
            elif carro_vermelho == 3:
                pos_x = 254
                
        if laranja_fora == False:
            if lary < -170:
                lary = 668
                if carro_vermelho == 1:
                    carro2 = randint(2,3)
                    if carro2 == 2:
                        larx = 161
                    
                    else: 
                        larx = 254
                    
                elif carro_vermelho == 2:
                    carro2 = randint(2,3)
                    if carro2 == 2:
                        larx = 254
                    
                    else: 
                        larx = 68

                elif carro_vermelho == 3:
                    carro2 = randint(2,3)
                    if carro2 == 2:
                        larx = 161
                    
                    else: 
                        larx = 68
                    
        
        if verde_fora == False and laranja_fora == False:
            if very < -170:
                very = 668
                if carro_vermelho == 1 and carro2 == 2 or carro_vermelho == 2 and carro2 == 1:
                    verx = 254

                elif carro_vermelho == 2 and carro2 == 2 or carro_vermelho == 3 and carro2 == 2:
                    verx = 68

                else:
                    verx = 161

        if laranja_fora == True and verde_fora == False:
            i = randint(0,2)
            if very + 159 <= 0:
                very = 520
                if pos_x == 68:
                    i = randint(0,1)
                    if i == 0:
                        verx = 161
                    else:
                        verx = 254
                if pos_x == 161:
                    i = randint(0,1)
                    if i == 0:
                        verx = 68
                    else:
                        verx == 254
                if pos_x == 254:
                    i = randint(0,1)
                    if i == 0:
                        verx = 68
                    else:
                        verx = 161
            
    if laranja_fora == True and vermelho_fora == False and vermelho_fora == False or vermelho_fora == True and laranja_fora == False and vermelho_fora == False or vermelho_fora == True and verde_fora == False and laranja_fora == False:
        dois_no_jogo = True

    if laranja_fora == True and verde_fora == True or verde_fora == True and vermelho_fora == True or laranja_fora == True and vermelho_fora == True:
        um_no_jogo = True

    if dois_no_jogo == True:
        if vermelho_fora == True:
            i = randint(0,2)
            if very + 151 <= 0:
                very = 510
                if i == 0:
                    verx = 68
                if i == 1:
                    verx == 161
                if i == 2:
                    verx = 254
            if lary + 159 <= 0:
                lary = 520
                if verx == 68:
                    i = randint(0,1)
                    if i == 0:
                        larx = 161
                    else:
                        larx = 254
                if verx == 161:
                    i = randint(0,1)
                    if i == 0:
                        larx = 68
                    else:
                        larx == 254
                if verx == 254:
                    i = randint(0,1)
                    if i == 0:
                        larx = 68
                    else:
                        larx = 161
        if laranja_fora == True:
            i = randint(0,2)
            if very + 151 <= 0:
                very = 510
                if i == 0:
                    verx = 68
                if i == 1:
                    verx == 161
                if i == 2:
                    verx = 254
            if pos_y + 159 <= 0:
                pos_y = 520
                if verx == 68:
                    i = randint(0,1)
                    if i == 0:
                        pos_x = 161
                    else:
                        pos_x = 254
                if verx == 161:
                    i = randint(0,1)
                    if i == 0:
                        pos_x = 68
                    else:
                        pos_x == 254
                if verx == 254:
                    i = randint(0,1)
                    if i == 0:
                        pos_x = 68
                    else:
                        pos_x = 161
        if verde_fora == True:
            i = randint(0,2)
            if pos_y + 151 <= 0:
                pos_y = 510
                if i == 0:
                    pos_x = 68
                if i == 1:
                    pos_x == 161
                if i == 2:
                    pos_x = 254
            if lary + 159 <= 0:
                lary = 520
                if pos_x == 68:
                    i = randint(0,1)
                    if i == 0:
                        larx = 161
                    else:
                        larx = 254
                if pos_x == 161:
                    i = randint(0,1)
                    if i == 0:
                        larx = 68
                    else:
                        larx == 254
                if pos_x == 254:
                    i = randint(0,1)
                    if i == 0:
                        larx = 68
                    else:
                        larx = 161
    
    if um_no_jogo == True:
        if laranja_fora == False:
           if lary + 159 <= 0:
                i = randint(0,2)
                if i == 0:
                    larx = 68
                if i == 1:
                    larx = 161
                if i == 2:
                    larx = 254
        if verde_fora == False:
            if very + 151 <= 0:
                i = randint(0,2)
                if i == 0:
                    verx = 68
                if i == 1:
                    verx = 161
                if i == 2:
                    verx = 254

    if um_no_jogo == True:
        if policia != policiaaberta:
            policia = policia1
            arma = 0

    if x <= 56:
        x = 56
    elif x >= 266:
        x = 266
    if y <= 0 and fora_do_carro == False:
        y = 0 
    if arma == 1:
        if y >= 316:
            y = 316 
    else:
        if y >= 360:
            y = 360

    if x <= 54:
        x = 55

            
    if pos_y >= 5000:
        velocidade_vermelho = 0
    if very >= 5000:
        velocidade_verde = 0
    if lary >= 5000:
        velocidade_laranja = 0


            

    if fora_do_carro == False:
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_c]:
            if porta == 1:
                if freio == True:
                    policia = policiaaberta
                    porta = 0
                    fora_do_carro = True
                    mostrar_carro = True
            else:
                policia = policia1
                porta = 1
        if comandos[pygame.K_SPACE]:
            
            if freio == False:
                freio = True
                andando = False
                eua = 1
                eua0 = 0
                policia = policia1
            else:
                freio = False
                andando = True
                eua = 0
            if stop == False:
                if velocidade_verde > 0:
                    velocidade_verde = 15
                if velocidade_vermelho > 0:
                    velocidade_vermelho = 15
                if velocidade_laranja > 0:
                    velocidade_laranja = 15
                stop = True
            else:
                if velocidade_verde > 0:
                    velocidade_verde = 5
                if velocidade_vermelho > 0:
                    velocidade_vermelho = 5
                if velocidade_laranja > 0:
                    velocidade_laranja = 5
                stop = False

            
    if andando == True:

        fundao += 1
        if fundao == 3:
            fundao = 0
        if fundao == 0:
            fundo = fundo0
        elif fundao == 1:
            fundo = fundo1
        elif fundao == 2:
            fundo = fundo2

 
    if fora_do_carro == True: 
        arma = 0
        comandos = pygame.key.get_pressed()       
        if mostrar_carro == True:
            mostrar_carro = False
            janela.blit(fp,(x + 83, y + 56))
            bx = x + 83
            by = y + 56
            msx = 999
            msy = 999

        if tiro_alto == True:
            cont += 1
            if cont == 4:
                cont = 0

            msy -= velocidade_missil
            if cont == 0:
                janela.blit(missil1,(msx,msy))
            if cont == 1:
                janela.blit(missil1,(msx,msy))
            if cont == 2:
                janela.blit(missil2,(msx,msy))
            if cont == 3:
                janela.blit(missil2,(msx,msy))

        if tiro_baixo == True:
            cont += 1
            if cont == 4:
                cont = 0

            msy += velocidade_missil
            if cont == 0:
                janela.blit(missil1b,(msx,msy))
            if cont == 1:
                janela.blit(missil1b,(msx,msy))
            if cont == 2:
                janela.blit(missil2b,(msx,msy))
            if cont == 3:
                janela.blit(missil2b,(msx,msy))
        
        if tiro_esquerda == True:
            cont += 1
            if cont == 4:
                cont = 0

            msx -= velocidade_missil
            if cont == 0:
                janela.blit(missil1e,(msx,msy))
            if cont == 1:
                janela.blit(missil1e,(msx,msy))
            if cont == 2:
                janela.blit(missil2e,(msx,msy))
            if cont == 3:
                janela.blit(missil2e,(msx,msy))

        if tiro_direita == True:
            cont += 1
            if cont == 4:
                cont = 0

            msx += velocidade_missil
            if cont == 0:
                janela.blit(missil1d,(msx,msy))
            if cont == 1:
                janela.blit(missil1d,(msx,msy))
            if cont == 2:
                janela.blit(missil2d,(msx,msy))
            if cont == 3:
                janela.blit(missil2d,(msx,msy))


        if msx + 40 >= pos_x and msx + 40 < pos_x + 150 and msy + 59 >= pos_y and msy + 59 < pos_y + 150:
            cve += 1
            if cve == 1:
                pos_x -= 41
                cont = 5
                velocidade_vermelho = 0
                vermelho = explosao
        if vermelho == explosao:
            if bx + 37 >= pos_x and bx + 37 < pos_x + 150 and msy + 34 >= pos_y and msy + 34 < pos_y + 150:
                time.sleep(2)
                perdeu = True
                break

            cvv += 1
            if cvv == 50:
                vermelho_explodiu = True
                
        if msx + 40 >= verx and msx + 40 < verx + 150 and msy + 59 >= very and msy + 59 < very + 150:
            cvee += 1
            if cvee == 1:
                verx -= 41
                cont = 5
                velocidade_verde = 0
                verde = explosao
        if verde == explosao:
            if bx + 37 >= verx and bx + 37 < verx + 150 and msy + 34 >= very and msy + 34 < very + 150:
                time.sleep(2)
                perdeu = True
                break
                
            cv += 1
            if cv == 50:
                verde_explodiu = True
        
        if msx + 40 >= larx and msx + 40 < larx + 159 and msy + 59 >= lary and msy + 59 < lary + 159:
            cle += 1
            if cle == 1:
                larx -= 41
                cont = 5
                velocidade_laranja = 0
                laranja = explosao
        if laranja == explosao:
            if bx + 37 >= verx and bx + 37 < verx + 150 and msy + 34 >= very and msy + 34 < very + 150:
                time.sleep(2)
                perdeu = True
                break
                
            cl += 1
            if cl == 50:
                laranja_explodiu = True
        

        if bx + 37 >= x and bx < x + 61 and by + 34 > y and by < y + 143:
            if bx + 37 >= x and bx + 30 < x:
                bx = x - 38
            elif bx <= x + 64 and x + 55 < bx:
                bx = x + 64
            elif by <= y + 144 and by > y:
                by = y + 145
            elif by + 34 >= y and y > by + 24:
                by = y - 34
        
        if bx <= 52:
            bx = 53 
        if bx + 37 >= 331:
            bx = 330 - 37
        if by <= 0:
            by = 0
        if by + 34 >= 500:
            by = 500 - 34
        
        if bx + 37 >= pos_x and pos_x + 70 >= bx and by + 34 >= pos_y and pos_y + 150 >= by:
            velobon = 0
            bl = atropelado
            bp = atropelado
            br = atropelado 
            bt = atropelado
            dl = atropelado
            dp = atropelado
            dr = atropelado
            dt = atropelado
            el = atropelado
            ep = atropelado
            er = atropelado
            et = atropelado
            fl = atropelado
            fp = atropelado
            fr = atropelado
            ft = atropelado 
           
            perdeu = True
                      
        if bx + 37 >= larx and larx + 72 >= bx and by + 34 >= lary and lary + 159 >= by:
            velobon = 0
            bl = atropelado
            bp = atropelado
            br = atropelado 
            bt = atropelado
            dl = atropelado
            dp = atropelado
            dr = atropelado
            dt = atropelado
            el = atropelado
            ep = atropelado
            er = atropelado
            et = atropelado
            fl = atropelado
            fp = atropelado
            fr = atropelado
            ft = atropelado
            
            perdeu = True
            
        if bx + 37 >= verx and verx + 71 >= bx and by + 34 >= very and very + 151 >= by:
            velobon = 0
            bl = atropelado
            bp = atropelado
            br = atropelado 
            bt = atropelado
            dl = atropelado
            dp = atropelado
            dr = atropelado
            dt = atropelado
            el = atropelado
            ep = atropelado
            er = atropelado
            et = atropelado
            fl = atropelado
            fp = atropelado
            fr = atropelado
            ft = atropelado
            perdeu = True
            
        
        if x + 69 >= msx and msx + 23 >= x and y + 140 >= msy and msy + 59 >= y:
            policia = explosao
            perdeu = True
            


        if bx >= x + 64 and bx < x + 70 and by + 34 > y + 28 and by < y + 64:
            fora_do_carro = False
        
        if event.type != pygame.KEYDOWN:
            if posicao == 1:
                janela.blit(fp,(bx,by))
            if posicao == 2:
                janela.blit(bp,(bx,by))
            if posicao == 3:
                janela.blit(ep,(bx,by))
            if posicao == 4:
                janela.blit(dp,(bx,by))
        
        if comandos[pygame.K_UP]:
            stick += 1
            if stick == 4:
                stick = 0
            by -= velobon
            if stick == 0:
                janela.blit(fr,(bx,by))
            if stick == 1:
                janela.blit(fr,(bx,by))
            if stick == 2:
                janela.blit(fl,(bx,by))
            if stick == 3:
                janela.blit(fl,(bx,by))
            posicao = 1
        elif comandos[pygame.K_DOWN]:
            
            stick += 1
            if stick == 4:
                stick = 0
            by += velobon
            if stick == 0:
                janela.blit(br,(bx,by))
            if stick == 1:
                janela.blit(br,(bx,by))
            if stick == 2:
                janela.blit(bl,(bx,by))
            if stick == 3:
                janela.blit(bl,(bx,by))
            posicao = 2
        elif comandos[pygame.K_LEFT]:
            stick += 1
            if stick == 4:
                stick = 0
            bx -= velobon
            if stick == 0:
                janela.blit(er,(bx,by))
            if stick == 1:
                janela.blit(er,(bx,by))
            if stick == 2:
                janela.blit(el,(bx,by))
            if stick == 3:
                janela.blit(el,(bx,by))
            posicao = 3
        elif comandos[pygame.K_RIGHT]:
            stick += 1
            if stick == 4:
                stick = 0
            bx += velobon
            if stick == 0:
                janela.blit(dr,(bx,by))
            if stick == 1:
                janela.blit(dr,(bx,by))
            if stick == 2:
                janela.blit(dl,(bx,by))
            if stick == 3:
                janela.blit(dl,(bx,by))
            posicao = 4 
        elif velobon != 0:
            if comandos[pygame.K_x]:
                cont = 0
                msy = by + 53 - 59
                msx = bx + 10
                if posicao == 1:
                    janela.blit(ft,(bx,by))
                    tiro_alto = True
                else: 
                    tiro_alto = False
                if posicao == 2:
                    janela.blit(bt,(bx,by))
                    tiro_baixo = True
                else:
                    tiro_baixo = False
                if posicao == 3:
                    janela.blit(et,(bx,by))
                    tiro_esquerda = True
                else:
                    tiro_esquerda = False
                if posicao == 4:
                    janela.blit(dt,(bx,by))
                    tiro_direita = True
                else:
                    tiro_direita = False
            
    if colisao != 0 and fora_do_carro == False:
        eua = 0

    pos_y -= velocidade_vermelho
    lary -= velocidade_laranja
    very -= velocidade_verde

    

    janela.blit(policia,(x,y))
    if vermelho_explodiu == False:
        janela.blit(vermelho,(pos_x, pos_y))
    if verde_explodiu == False:
        janela.blit(verde,(verx, very))
    if laranja_explodiu == False:
        janela.blit(laranja,(larx, lary))



    
    
    pygame.display.update()

pygame.quit()
