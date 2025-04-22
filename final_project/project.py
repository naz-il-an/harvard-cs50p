import pygame
import time
import random

screen_width = 480
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 5
SNAKE_SIZE = 10
score = 0
x = int((screen_width/SNAKE_SIZE)/2) * SNAKE_SIZE
y = int((screen_height/SNAKE_SIZE)/2) * SNAKE_SIZE 
snake_length = 1
snake_list = [[x, y]]

def main():
    global fps, score, x, y, snake_length
    pygame.init()
    
    clock = pygame.time.Clock()
    pygame.display.set_caption('Snake CS50 Game')    
    
    bg = pygame.Surface((screen_width,screen_height))
    bg.fill((0,0,0))   
    
    dx, dy = 0, -1
    right, left, up, down = True, True, True, True 
    x_food, y_food = food_position()
    
    status = True
    while status:
        screen.blit(bg, (0,0))
        show_score()
        x += dx * SNAKE_SIZE
        y += dy * SNAKE_SIZE 
        draw_snake()
        pygame.draw.circle(screen, pygame.Color('blue'), [x_food + SNAKE_SIZE/2, y_food + SNAKE_SIZE/2], SNAKE_SIZE/2)
        if x == x_food and y == y_food:
            score +=1
            snake_length +=1           
            pygame.display.flip()
            x_food, y_food = food_position()
        
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_over()
            pygame.display.flip()            
            time.sleep(5)
            status = False

        head = [x, y]
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        elongate_snake(snake_list)
        for block in snake_list[:-1]:
            if block == head:
                game_over()
                pygame.display.flip()                
                time.sleep(5)
                status = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and left:
                    dx, dy = -1, 0  
                    right, left, up, down = False, True, True, True
                elif event.key == pygame.K_RIGHT and right:
                    dx, dy = 1, 0  
                    right, left, up, down = True, False, True, True
                elif event.key == pygame.K_UP and up:                    
                    dx, dy = 0, -1  
                    right, left, up, down = True, True, True, False
                elif event.key == pygame.K_DOWN and down:                                        
                    dx, dy = 0, 1                    
                    right, left, up, down = True, True, False, True
        
        pygame.display.flip()
        clock.tick(fps)    

def draw_snake():
    pygame.draw.rect(screen,pygame.Color('green'), [x, y, SNAKE_SIZE, SNAKE_SIZE])

def elongate_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen,pygame.Color('green'), [block[0], block[1], SNAKE_SIZE, SNAKE_SIZE])

def food_position():
    x_food = random.randrange(1, int(screen_width/SNAKE_SIZE)) * SNAKE_SIZE
    y_food = random.randrange(1, int(screen_height/SNAKE_SIZE)) * SNAKE_SIZE
    return x_food, y_food

def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render('Score: ' + str(score), True, pygame.Color('white'))
    screen.blit(text, [10,10])

def game_over():
    global score
    font = pygame.font.SysFont(None, 40)
    text = font.render('GAME OVER', True, pygame.Color('red'))
    text2 = font.render(f'Score: {score}', True, pygame.Color('red'))
    screen.blit(text, [screen_height/2-20, screen_height/2 - 20])
    screen.blit(text2, [screen_height/2-15, screen_height/2 + 10])
             

if __name__ == '__main__':
    main()