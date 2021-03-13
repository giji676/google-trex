from canvas.constants import WIDTH, HEIGHT, BLACK, GREY
from canvas.obstacles import Obstacles
from canvas.player import Player
from canvas.board import Board
import time
import pygame

FPS = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHROME/GOOGLE dino game")
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
pygame.font.init()
hp = 3
speed = 15
high_score = 0
score = 0

f_a = open("high_score.txt", "a")
f_a.close()


def main():
    global FPS, hp, speed, high_score, score
    run = True
    clock = pygame.time.Clock()
    board = Board()
    player = Player()
    obstacle = Obstacles()

    while run:
        speed += 0.001
        FPS += 0.001
        board.ground_x -= speed

        score += 1
        f_r = open("high_score.txt", "r")
        for line in f_r:
            if float(line) > high_score:
                high_score = float(line)
        f_r.close()
        board.draw_ground(WIN)
        board.draw_ground_dots()
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        font = pygame.font.SysFont("Arial", 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not player.jumping:
            if key[pygame.K_w]:
                player.jump_true()
        else:
            if player.jump_count >= -10:
                player.jump()
            else:
                player.jumping = False
                player.jump_count = 10

        obstacle.chose_random_obstacle()
        obstacle.x -= speed
        if player.hitbox[0] + player.hitbox[2] >= obstacle.hitbox[0]:
            if player.hitbox[1] + player.hitbox[3] >= obstacle.hitbox[1]:
                if obstacle.hitbox[0] + obstacle.hitbox[2] <= 50:
                    pass
                else:
                    if hp == 1:
                        f_a = open("high_score.txt", "a")
                        f_a.write(str(score/10) + "\n")
                        f_a.close()
                        font_ = pygame.font.SysFont("Arial", 80)
                        font = pygame.font.SysFont("Arial", 30)
                        text = font_.render("Game over", 1, GREY)
                        high_score_text_death = font.render("final score: " + str(int(score/10)), 1, GREY)
                        WIN.blit(text, (500 - int(text.get_width() / 2), 300 - int(text.get_height() / 2)))
                        WIN.blit(high_score_text_death, (500 - int(high_score_text_death.get_width() / 2), 350))
                        score = 0
                        FPS = 30
                        speed = 15
                        pygame.display.update()
                        time.sleep(2.5)
                        obstacle.x = WIDTH
                        main()
                    else:
                        hp -= 1
                        f_a = open("high_score.txt", "a")
                        f_a.write(str(score/10) + "\n")
                        f_a.close()
                        font = pygame.font.SysFont("Arial", 80)
                        text = font.render("-1 hp", 1, GREY)
                        WIN.blit(text, (500 - int(text.get_width() / 2), 300 - int(text.get_height() / 2)))
                        pygame.display.update()
                        pygame.display.update()
                        time.sleep(1)
                        obstacle.x = WIDTH
                        main()

        if obstacle.x <= 0 - obstacle.hitbox[2]:
            obstacle.x = WIDTH
            obstacle.new_obstacle()
            obstacle.chose_random_obstacle()

        print(speed, FPS)

        text = font.render("score: " + str(int(score / 10)), 1, BLACK)
        high_score_text = font.render("highest score: " + str(int(high_score)), 1, BLACK)
        hp_count = font.render("hp " + str(hp) + "/3", 1, BLACK)

        WIN.blit(hp_count, (800, 50))
        WIN.blit(text, (500 - int(text.get_width() / 2), 50))
        WIN.blit(high_score_text, (50, 50))

        player.draw_player()
        pygame.display.update()

    pygame.quit()


main()
