import pygame
from pygame.locals import *
from solve import validate


size = 480, 480
s_width , s_height = size
width, height = 50,50
margin = 3

green = (150,255,150)
red = (255,0,0)
grey = (150,150,150)
black  = (0,0,0)
white = (255,255,255)




image = {}
def load_image():
    for i in range(10):
        image[i] = pygame.image.load('img/0'+str(i)+'.png')
load_image()


def grid_draw(gri):
    for row_ in range(9):
        for column_ in range(9):
            color = white
            pygame.draw.rect(screen,color,
                             [(margin + width) * column_ + margin,
                              (margin + height) * row_ + margin,
                              width,
                              height])
            lis = [159,318]
            for i in lis:
                pygame.draw.line(screen,red,(0,i),(s_width,i),margin)
                pygame.draw.line(screen,red,(i,0),(i,s_height),margin)



matrix = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
grid =[]
for row in range(9):
    grid.append([])
    for column in range(9):
        grid[row].append(0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Suduku")
running = True

clock = pygame.time.Clock()

def solving(matrix):
    screen.fill(black)
    grid_draw(matrix)
    for p in range(9):
        for q in range(9):
            if matrix[p][q] != 0:
                x, y = (margin + width) * p + margin, (margin + height) * q + margin
                screen.blit(image[matrix[p][q]], (y, x))
    #clock.tick(10)
    for i in range(0,9):
        for j in range(0,9):
            clock.tick(500)
            if matrix[i][j] == 0:
                for k in range(1,10):
                    if validate(k,i,j,matrix):
                        matrix[i][j] = k
                        x, y = (margin + width) * i + margin, (margin + height) * j + margin
                        screen.blit(image[k], (y, x))
                        #clock.tick(1000)
                        pygame.display.update()
                        if solving(matrix):
                            return True
                        matrix[i][j] = 0
                return False
    return True
draw = True
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                draw = False



    # Movement


    # Drawing Section

    if not draw:
        draw = solving(matrix)

    screen.fill(black)
    grid_draw(matrix)
    for p in range(9):
        for q in range(9):
            if matrix[p][q] != 0:
                x, y = (margin + width) * p + margin, (margin + height) * q + margin
                screen.blit(image[matrix[p][q]], (y, x))
    pygame.display.update()


pygame.quit()
