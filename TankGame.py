import pygame
import random
import math
pygame.init()
d_w=840                                                  #display width of screen
d_h=600                                                  #display height of screen
sc=pygame.display.set_mode((d_w,d_h))                    #dispalying screen of d_w width and d_w height                                  
clock=pygame.time.Clock()                                #creting clock to control FPS
Smallfont=pygame.font.SysFont('comicsansms',30)          #describing font of small size
Mediumfont=pygame.font.SysFont('comicsansms',35)         #describing font of medium size
Largefont=pygame.font.SysFont('comicsansms',100)          #describing font of large size
dm=0
de=0
FPS=15                                                   #frame per second 
color=[(255,255,0),(255,0,0),(220,0,0),(150,0,0),(200,0,0),(225,125,0),(200,100,0)]
pygame.display.set_caption('Tanks')


def Button(color,x,y,w,h,txt,extrasize=0):
	pygame.draw.rect(sc,color,(x,y,w+extrasize,h))
	st=Smallfont.render(txt,True,(255,255,255))
        sc.blit(st,[x+7,y+7]) 
	 
	pygame.display.update()

def tank(x,y,pos):
	t=[(x-27, y-2),
           (x-26, y-5),
           (x-25, y-8),
           (x-23, y-12),
           (x-20, y-14),
           (x-18, y-15),
           (x-15, y-17),
           (x-13, y-19),
           (x-11, y-21)]
	if pos>8:
	    pos=8
	elif pos<0:
	    pos=0
	pygame.draw.circle(sc,(0,0,0),(x,y),10)
	pygame.draw.rect(sc,(0,0,0),(x-16,y-2,35,15))
	pygame.draw.line(sc,(0,0,0),(x,y),t[pos],3)
	pygame.draw.circle(sc,(0,0,0),(x-12,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-6,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-9,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-3,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+3,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+6,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+9,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+12,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+15,y+15),3)
	return t[pos],pos+1

def enemytank(x,y,pos):
	t=[(x+27, y-2),
           (x+26, y-5),
           (x+25, y-8),
           (x+23, y-12),
           (x+20, y-14),
           (x+18, y-15),
           (x+15, y-17),
           (x+13, y-19),
           (x+11, y-21)]
	if pos>8:
	    pos=8
	elif pos<0:
	    pos=0
	pygame.draw.circle(sc,(0,0,0),(x,y),10)
	pygame.draw.rect(sc,(0,0,0),(x-16,y-2,35,15))
	pygame.draw.line(sc,(0,0,0),(x,y),t[pos],3)
	pygame.draw.circle(sc,(0,0,0),(x-12,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-6,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-9,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x-3,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+3,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+6,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+9,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+12,y+15),3)
	pygame.draw.circle(sc,(0,0,0),(x+15,y+15),3)
	return t[pos],pos+1


def barrier(b_x,b_y):
    pygame.draw.rect(sc,(255,0,0),(b_x,d_h-b_y,50,b_y))
    for i in range(d_h-b_y):
			pygame.draw.line(sc,(255,255,255),(b_x,d_h-b_y),(b_x+50,d_h-b_y+50),3)
	
			b_y-=6
	
	
def power(level):
    text = Smallfont.render("Power_X: "+str(level)+"%",True, (0,0,0))
    sc.blit(text, [d_w/2-90,0])


def power2(level):
    text = Smallfont.render("Power_Y: "+str(level)+"%",True, (0,0,0))
    sc.blit(text, [d_w/2+50,0])



'''def healthbar(dmt,det):
	life_mt=100-dmt
	life_et=100-det
	if life_mt>75:
		colors=(0,255,0)
	elif life_mt>50:
		colors=(255,255,0)
	else:
		colors=(255,0,0)
	
	if life_et>75:
		color_e=(0,255,0)
	elif life_et>50:
		color_e=(255,255,0)
	else:
		color_e=(255,0,0)
	pygame.draw.rect(sc,colors,(680,0,life_mt,25))

	pygame.draw.rect(sc,color_e,(30,0,life_et,25))	
	pygame.display.update()'''



def explosion(x, y, size=50):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [(255,255,0),(255,0,0),(220,0,0),(150,0,0),(200,0,0),(225,125,0),(200,100,0)]

        magnitude = 1

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(sc, colorChoices[random.randrange(0,4)], (exploding_bit_x,exploding_bit_y),random.randrange(1,5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False




	

        
def e_fireShell2(xy,tankx,tanky,turPos,xlocation,randomHeight,ptankx,ptanky):

    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        #print(currentPower)

        fire = True
        startingShell = list(xy)


        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            

            startingShell[0] += (12 - turPos)*2
            startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50.0))**2) - (turPos+turPos/(12-turPos)))

            if startingShell[1] > d_h-15:
                hit_x = int((startingShell[0]*d_h-25)/startingShell[1])
                hit_y = int(d_h-25)
                
                if ptankx+15 > hit_x > ptankx - 15:
                    print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + 70
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= d_h
            check_y_2 = startingShell[1] >= d_h - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                
                fire = False
    

    
    fire = True
    startingShell = list(xy)
    print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        pygame.draw.circle(sc, (255,255,255), (startingShell[0],startingShell[1]),5)


        startingShell[0] += (12 - turPos)*2



     
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50.0))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > d_h-15:
            print("last shell:",startingShell[0],startingShell[1])
            hit_x = int((startingShell[0]*d_h-25)/startingShell[1])
            hit_y = int(d_h-25)
            print("Impact:",hit_x,hit_y)
            if ptankx + 15 > hit_x > ptankx - 15:
                print("HIT TARGET!")
                de += 25
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + 70
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= d_h
        check_y_2 = startingShell[1] >= d_h - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False

        
        

        pygame.display.update()
        clock.tick(60)
    return de




	

		
def fireShell2(xy,tankx,tanky,turPos,gun_power,py,b_x,b_y,ptankx,ptanky):
    
    fire = True
    startingShell = list(xy)
    print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        pygame.draw.circle(sc, (255,255,255), (startingShell[0],startingShell[1]),5)


        startingShell[0] -= (12 - turPos)*2



     
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50.0))**2) - (turPos+py+turPos/(12-turPos)))

        if startingShell[1] > d_h-15:
            hit_x = int((startingShell[0]*d_h-25)/startingShell[1])
            hit_y = int(d_h-25)
            print("Impact:",hit_x,hit_y)
            if ptankx + 15 > hit_x > ptankx - 15:
                print("HIT TARGET!")
               
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= b_x + 70
        check_x_2 = startingShell[0] >= b_x

        check_y_1 = startingShell[1] <= d_h
        check_y_2 = startingShell[1] >= d_h - b_y

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False



        pygame.display.update()
        clock.tick(60)
    




 
def control():
	sc.fill((125,0,125))
	on=True
	while on:
		message_to_screen("Rules", (25,255,121),130,-120,Largefont)
		message_to_screen("@  Destroy the enemy tanls before they destroy you", (255,255,255), -45,0,Smallfont)
		message_to_screen("@   Press Spacebar to fire your Cannon.", (255,255,255), -45,30,Smallfont)	
		message_to_screen('@  Press A to increase horizontal power and L to decrease Horizontal power ',(255,255,255), -45,60,Smallfont)
		message_to_screen('@  Press S to increase Vertical  power and K to decrease Vertical power ',(255,255,255), -45,90,Smallfont)
		message_to_screen('@  Buttons are given to you for your help !!  ',(255,255,255), -45,120,Smallfont)	
		message_to_screen("@  Press Z to exit the Rules page.", (255,255,255), -45,150,Smallfont)		
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_z:
					game_intro()
					
		pygame.display.update()
	#clock.tick(60)
	
	
def gameloop(): 
    
    img = pygame.image.load('index.jpeg')
    pow,py=50,0
    gameover=False                                        #gives a choice to play again
    gameExit=False                                        #variable controoling main loop of game
    xi,yi=690, 540
    changeTur=0
    b_x= (d_w//2)-random.randint(-0.2*d_w,0.2*d_w)      #barrier x coordinate
    b_y= (random.randint(0.1*d_h,0.6*d_h))            #barrier y coordinate
    
    while not gameExit: 
			sc.fill((34,177,76))
			img = pygame.transform.scale(img, (d_w, d_h))
			sc.blit(img,(0,0))
		
			barrier(b_x,b_y)
			if xi-(35//2)<b_x+50:     #so that tank do not goes inside barrier
				xi+=5
			power(pow)
			power2(py)
			#healthbar(dm, de)
			gun , pos =tank(int(xi),int(yi),changeTur)	
			gune,pose=enemytank(40,540,changeTur)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						xi+= -5
					elif event.key == pygame.K_RIGHT:
						xi+= 5
					elif event.key==pygame.K_l:
						pow-=3
						print(pow)
					elif event.key==pygame.K_a:
						pow+=3
						print(pow)
					elif event.key == pygame.K_UP:
						changeTur += 1
					elif event.key == pygame.K_DOWN:
						changeTur += -1
					elif event.key == pygame.K_s:
						py+=0.3
					elif event.key == pygame.K_k:
						py-=0.3
					elif event.key == pygame.K_SPACE:
						
						fireShell2(gun,int(xi),int(yi),pos,pow,py,b_x,b_y,40,540)
						dm=e_fireShell2(gune,40,540,pose,b_x,b_y,int(xi),int(yi))
						
					elif event.key == pygame.K_p:
						pause()
			cur=pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if 693<cur[0]<693+65 and 560<cur[1]<560+40:
				Button((0,0,255),693,560,65,40,"Quit") 
				if click[0]==1:
					pygame.quit()
					quit()
			else:
				Button((0,0,195),693,560,65,40,"Quit")  


			if 757<cur[0]<757+65 and 560<cur[1]<560+40:
				Button((34,177,76),757,560,65,40,"Pause",20) 
				if click[0]==1:
					pause() 
			else:
				Button((195,195,0),757,560,65,40,"Pause",20)            
		
			pygame.display.update()


			if gameover == True:
				sc.fill((0,0,0))
				cur=pygame.mouse.get_pos()
				click = pygame.mouse.get_pressed()
				if 360<cur[0]<360+65 and 514<cur[1]<514+40:
					Button((255,255,0),360,514,65,40,"Replay",20) 
					if click[0]==1:
						gameloop() 
				else:
					Button((195,195,0),360,514,65,40,"Replay",20) 

				if 622<cur[0]<622+65 and 514<cur[1]<514+40:
					Button((0,0,255),622,514,65,40,"Quit") 
					if click[0]==1:
						pygame.quit()
						quit()
				else:
					Button((0,0,195),622,514,65,40,"Quit")

				message_to_screen("Game over", (255,0,0),-150,Largefont)
				message_to_screen("Your Score "+str(score), (255,255,0),-80,Largefont)
				message_to_screen('press C to play again or Q to quit',(255,255,255),20,Mediumfont)
				pygame.display.update()

			clock.tick(FPS)





def game_intro():
    img1 = pygame.image.load('tank.jpeg')
    img2 = pygame.image.load('tank1.jpeg')
    img3 = pygame.image.load('tank5.jpeg')    
    intro=True
    while intro:
        sc.fill((255,255,255))

	sc.blit(img1,(0,0))
	sc.blit(img2,(284,0))
	sc.blit(img3,(284+300,0))
        message_to_screen("WELCOME TO TANKS",(34,177,76),-70,-100,Largefont)
        message_to_screen("Its a tank game.",(0,0,0),130,0,Mediumfont)
        message_to_screen("Destroy enemy tanks before they destroy you.",(0,0,0),20,40,Mediumfont) 
        message_to_screen("The more tanks you destroy,the harder it get.Hope you enjoy it.",(0,0,0),-55,80,Mediumfont) 
	cur=pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 110<cur[0]<110+65 and 490<cur[1]<490+40:
	    Button((34,177,76),110,490,65,40,"Play")  
	    if click[0]==1:
		gameloop()
	else:
	    Button((195,0,0),110,490,65,40,"Play")

	      
     	if 340<cur[0]<340+65 and 490<cur[1]<490+40:
	    Button((34,177,76),340,490,65,40,"Rules",20) 
	    if click[0]==1:
		control()	

	else:
	    Button((195,195,0),340,490,65,40,"Rules",20) 


	if 600<cur[0]<600+65 and 490<cur[1]<490+40:
	    Button((34,177,76),600,490,65,40,"Quit") 
	    if click[0]==1:
	        pygame.quit()
                quit()
	else:
	    Button((0,0,195),600,490,65,40,"Quit")     
	     
        for event in pygame.event.get():       #direct exit from the game
	    
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    intro=False
		    
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()        
        pygame.display.update()
        clock.tick(4)


def message_to_screen(msg,color,shiftl,shiftr,size):
    screen_text=size.render(msg,True,color)
    sc.blit(screen_text,[110+shiftl,d_h//2+shiftr])               #adding text in middle of screen




def pause():
    paused=True
    message_to_screen("PAUSED GAME",(255,0,0),0,-100,Largefont)
    message_to_screen("press P to continue and q to quit",(0,0,0),0,0,Mediumfont)   
    
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
    clock.tick(5)

game_intro()


gameloop()
