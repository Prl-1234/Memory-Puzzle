import random,pygame,sys
from pygame.locals import *

GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
PINK=(255,165,0)
BLACK=(0,0,0)
WHITE=(255,255,255)

SQUARE='square'
DONUT='donut'
DIAMOND='diamond'
RECTANGLE='rectangle'

ALLCOLORS=(RED,GREEN,BLUE,PINK)
ALLSHAPES=(SQUARE,DONUT,DIAMOND)

def main():
    pygame.init()
    FPS=30
    FPSCLOCK=pygame.time.Clock()
    SURFACE=pygame.display.set_mode((500,500))
    pygame.display.set_caption('MEMORY GAME')
    SURFACE.fill((255,255,255))
    icons=[]
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))
    random.shuffle(icons)
    numIconsUsed=12
    icons=icons[:numIconsUsed]*2
    random.shuffle(icons)
    board=[]
    revealed=[]
    for x in range(6):
        column=[]
        reveal=[]
        for y in range(4):
            column.append(icons[0])
            reveal.append(False)
            del icons[0]
        board.append(column)
        revealed.append(reveal)
    for boxx in range(6):
        for boxy in range(4):
            left=boxx*60+70
            top=boxy*80+90
            shape,color=board[boxx][boxy][0],board[boxx][boxy][1]
            if shape==SQUARE:
                pygame.draw.rect(SURFACE,color,(left+1,top+1,58,78))
            elif shape==DONUT:
                pygame.draw.circle(SURFACE,color,(left+30,top+40),(29),2)
            else:
                pygame.draw.polygon(SURFACE,color,((left+30,top+1),(left+59,top+40),(left+30,top+79),(left+1,top+40)))
    x=0 
    y=0
    while True:
        x=x+1
        if x>2:
            z=0
            for boxx in range(6):
                for boxy in range(4):
                    left=boxx*60+70
                    top=boxy*80+90
                    if revealed[boxx][boxy]==True :
                        shape,color=board[boxx][boxy][0],board[boxx][boxy][1]
                        if shape==SQUARE:
                            pygame.draw.rect(SURFACE,color,(left+1,top+1,58,78))
                        elif shape==DONUT:
                            pygame.draw.rect(SURFACE,WHITE,(left+1,top+1,58,78))
                            pygame.draw.circle(SURFACE,color,(left+30,top+40),(29),2)
                        else:
                            pygame.draw.rect(SURFACE,WHITE,(left+1,top+1,58,78))
                            pygame.draw.polygon(SURFACE,color,((left+30,top+1),(left+59,top+40),(left+30,top+79),(left+1,top+40)))
                    else:
                        z=1
                        pygame.draw.rect(SURFACE,BLACK,(left+1,top+1,58,78))
            if z==0:
                pygame.display.set_caption('GAME COMPLETED!!')
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

    
            
        for event in pygame.event.get():
            if event.type==QUIT or event.type==KEYUP:
                pygame.quit()
                sys.exit() 
            elif event.type==MOUSEBUTTONUP:
                mx,my=event.pos
                for boxx in range(6):
                    for boxy in range(4):
                        left=boxx*60+70
                        top=boxy*80+90
                        boxRect=pygame.Rect(left,top,60,80)
                        if boxRect.collidepoint(mx,my) and revealed[boxx][boxy]==False:
                            if y==0:
                                revealed[boxx][boxy]=True 
                                firstx=boxx
                                firsty=boxy
                                y=1      
                            elif y==1:
                                y=0
                                revealed[boxx][boxy]=True
                                if board[boxx][boxy][0]==board[firstx][firsty][0] and  board[boxx][boxy][1]==board[firstx][firsty][1]:
                                    y=0
                                else:
                                    shape,color=board[boxx][boxy][0],board[boxx][boxy][1]
                                    if shape==SQUARE:
                                        pygame.draw.rect(SURFACE,color,(left+1,top+1,58,78))
                                    elif shape==DONUT:
                                        pygame.draw.rect(SURFACE,WHITE,(left+1,top+1,58,78))
                                        pygame.draw.circle(SURFACE,color,(left+30,top+40),(29),2)
                                    else:
                                        pygame.draw.rect(SURFACE,WHITE,(left+1,top+1,58,78))
                                        pygame.draw.polygon(SURFACE,color,((left+30,top+1),(left+59,top+40),(left+30,top+79),(left+1,top+40)))
                                    pygame.display.update()
                                    pygame.time.wait(500)
                                    revealed[boxx][boxy]=False
                                    revealed[firstx][firsty]=False                                    
        if x==2:
            pygame.time.wait(1000)        
            for boxx in range(6):
                for boxy in range(4):
                    left=boxx*60+70
                    top=boxy*80+90
                    if(revealed[boxx][boxy]==False):
                        pygame.draw.rect(SURFACE,BLACK,(left+1,top+1,58,78))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
if __name__=='__main__':
    main()