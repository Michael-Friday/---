import time
import pygame
import random

#初始化 pygame
pygame.init()
#success, failures = pygame.init()
#print(f"成功初始化 {success} 模組，失敗 {failures} 模組")

#視窗的長度、高度
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('貪食蛇')

#設定顏色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#定義遊戲參數
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 13

#設置字體
font_style = pygame.font.SysFont(None, 35)

#顯示分數訊息的參數
def show_score(score):
    value = font_style.render("Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

#顯示結束訊息的參數
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
    pygame.display.update()
    time.sleep(5)

#遊戲結束
def game_over_screen():
    screen.fill(blue)
    message("Game over Q=quit OR C=Again", red)
    pygame.display.update()
    waiting = True
    while waiting :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    waiting = False

#遊戲主循環
def game_loop():
    
    #初始蛇的位置和身體
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0
    snake_list = []
    length_of_snake = 1

    #食物的位置
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    running = True
    while running :
        #監視按鍵時間
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, snake_block
    
        #檢察是否出界
        if x>= width or x < 0 or y >= height or y < 0:
            game_over_screen()
            return #結束當前的game_loop並重啟遊戲
        x += x_change
        y += y_change

        #清除畫面並顯示食物
        screen.fill(black) 
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        
        #更新蛇的位置
        snake_head = [x,y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
    
        #檢查蛇是否會碰到自己
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over_screen()
                return 
    
        #畫出蛇的每個身體部分
        for segment in snake_list:
            pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])
        
        #顯示分數並更新畫面
        show_score(length_of_snake - 1)
        pygame.display.update()

        #如果蛇傳到食物， 延長蛇的長度並重新產生食物
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0 ) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0 ) * 10.0
            length_of_snake += 1
    

        # 控制遊戲速度
        clock.tick(snake_speed)

    pygame.quit()
    quit()

while True:
    game_loop()