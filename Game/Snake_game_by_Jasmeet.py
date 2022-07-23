import pygame
import random
import os
pygame.init()  # initializing all the modules of pygame module
pygame.mixer.init()

window_breadth = 800
window_height = 500
# colors
white = (255,255,255)
black =(0,0,0)
red = (255,0,0)
blue = (0,50,255)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe UI",35)

window = pygame.display.set_mode((window_breadth, window_height))
pygame.display.set_caption("Snakes with Jasmeet")
#background image
bgimg = pygame.image.load("back.jpg")
bgimg = pygame.transform.scale(bgimg,(window_breadth,window_height)).convert_alpha()

def text_display(text,color,x,y):
    # the method render() must be used to create a Surface object from the text, which then can be blit to the screen
    screen_text = font.render(text,True,color)
    window.blit(screen_text,[x,y])
def plot_snake(window,black,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(window,black,[x,y,snake_size,snake_size])
def welcome():
    exit_game = False
    while not exit_game:
        Start = pygame.image.load("Starting_img.jpg")
        Start = pygame.transform.scale(Start,(window_breadth,window_height)).convert_alpha()
        window.blit(Start,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Bck_grd.mp3.mp3')
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def game_loop():
    game_over = False
    quit_game = False
    snake_x = 45
    snake_y = 55
    food_x = random.randint(50, window_breadth // 2)
    food_y = random.randint(50, window_height // 2)
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    velocity_init = 5
    score = 0
    fps = 30
    snk_list = []
    snk_length = 1
    if (not os.path.exists("hi_score.txt")):
        with open("hi_score.txt","w") as f:
            f.write("0")
    with open("hi_score.txt","r") as f :
        hiscore = f.read()
    #game loop
    while not quit_game:
        if game_over:
            with open("hi_score.txt","w") as f :
                f.write(str(hiscore))
            over = pygame.image.load("game_end.jpg")
            over =pygame.transform.scale(over,(window_breadth,window_height)).convert_alpha()
            window.blit(over,(0,0))

            text_display(f"New Score:{score}",(150,190,10),window_breadth//3,window_height-400)
            for event in pygame.event.get(): # handling the events
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get(): # handling the events
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity_init
                        velocity_y =0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity_init
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y =-velocity_init
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = velocity_init
            snake_x = snake_x +velocity_x
            snake_y = snake_y +velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y-food_y) < 10:
                score = score + 10
                food_x = random.randint(50, window_breadth // 2)
                food_y = random.randint(50, window_height // 2)
                snk_length = snk_length +5
                if score > int(hiscore):
                    hiscore = score
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()
            window.fill(white)
            window.blit(bgimg,(0,0))
            if snake_x<0 or snake_x >window_breadth or snake_y<0 or snake_y>window_height:
                game_over = True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()
            plot_snake(window,black, snk_list, snake_size)
            pygame.draw.rect(window,red,[food_x,food_y,snake_size,snake_size])
            text_display(f"Score:{score} High score:{hiscore}", white, 5, 5)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()

welcome()
