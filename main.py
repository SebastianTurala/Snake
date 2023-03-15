import sys
import pygame
from random import randrange

pygame.init()
clock = pygame.time.Clock()

# window
width = 400
height = 400
window = pygame.display.set_mode((width, height))


while True:
    # snake
    snake_pos = [200, 200]
    snake_dir = ""
    snake_speed = 10
    snake_bod = [[200, 200]]
    # first gem
    gem_pos = [randrange(1, (height // 10)) * 10, randrange(1, (width // 10)) * 10]
    gem = True
    # game loop
    game_over = False
    # score
    score = 0
    score_speed = 0
    score_font = pygame.font.SysFont("Arial", 15)
    while not game_over:
        if snake_pos[0] <= 0 or snake_pos[0] >= width or snake_pos[1] <= 0 or snake_pos[1] >= height:
            game_over = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # direction keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if snake_dir == "R":
                        pass
                    else:
                        snake_dir = "L"
                elif event.key == pygame.K_RIGHT:
                    if snake_dir == "L":
                        pass
                    else:
                        snake_dir = "R"
                elif event.key == pygame.K_UP:
                    if snake_dir == "U":
                        pass
                    else:
                        snake_dir = "D"
                elif event.key == pygame.K_DOWN:
                    if snake_dir == "D":
                        pass
                    else:
                        snake_dir = "U"

        if snake_dir == "L":
            snake_pos[0] -= 10
        elif snake_dir == "R":
            snake_pos[0] += 10
        elif snake_dir == "D":
            snake_pos[1] -= 10
        elif snake_dir == "U":
            snake_pos[1] += 10

        snake_bod.insert(0, list(snake_pos))
        if snake_pos[0] == gem_pos[0] and snake_pos[1] == gem_pos[1]:
            score += 10
            score_speed += 10
            gem = False
        else:
            snake_bod.pop()

        if not gem:
            gem_pos = [randrange(1, (height//10)) * 10, randrange(1, (width//10)) * 10]
            gem = True

        for block in snake_bod[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over = True

        if score_speed == 50:
            snake_speed += 1
            score_speed = 0

        # score text
        score_text = score_font.render("Your Score: " + str(score), True, "black")
        window.blit(score_text, [0, 0])

        # gem draw
        pygame.draw.rect(window, "red", [gem_pos[0], gem_pos[1], 10, 10])

        # snake draw
        for pos in snake_bod:
            pygame.draw.rect(window, "black", [pos[0], pos[1], 10, 10])

        pygame.display.update()
        window.fill("white")
        clock.tick(snake_speed)