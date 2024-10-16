import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre + creation
hauteur = 800
largeur = 600
screen = pygame.display.set_mode((hauteur, largeur))
pygame.display.set_caption('Ck pong_game')
#mise du backgound
backgound=pygame.image.load("Documents\ck\ckfond.png").convert()
class raquette:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, y):
        self.rect.y += y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > hauteur:
            self.rect.bottom = hauteur

class balle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = 5
        self.speed_y = 5

    def deplacement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= hauteur:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= largeur:
            self.speed_x *= -1
def main():
    #l'ideale c'est d'utiliser l'anglais pour eviter les "not found by pylance"
    clock = pygame.time.Clock()
    paddle1= raquette(30, hauteur // 2 - 50)
    paddle2 = raquette(largeur- 40,hauteur // 2 - 50)
    ball= balle(largeur // 2, hauteur // 2)


    while True:
#appliquer le background sur le l'ecran
screen = pygame.display.set_mode((hauteur, largeur))
    screen.blit(backgound,(0,0))
#mettre a jour l'ecran
    pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-5)
        if keys[pygame.K_s]:
            paddle1.move(5)
        if keys[pygame.K_UP]:
            paddle2.move(-5)
        if keys[pygame.K_DOWN]:
            paddle2.move(5)

        ball.move()

        screen.fill(black)
        pygame.draw.rect(screen, white, paddle1.rect)
        pygame.draw.rect(screen, white, paddle2.rect)
        pygame.draw.ellipse(screen, white, ball.rect)
        pygame.draw.aaline(screen, white, (largeur // 2, 0), (largeur // 2, hauteur))

        pygame.display.flip()
        clock.tick(60)

    if __name__ == '__main__':
    main()
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)
def main():
    clock = pygame.time.Clock()
    paddle1 = raquette(30, hauteur // 2 - 50)
    paddle2 = raquette(largeur - 40, hauteur // 2 - 50)
    ball = Ball(largeur // 2, hauteur // 2)
    score1 = 0
    score2 = 0
    font = pygame.font.Font(None, 74)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            paddle1.move(-5)
        if keys[pygame.K_s]:
            paddle1.move(5)
        if keys[pygame.K_UP]:
            paddle2.move(-5)
        if keys[pygame.K_DOWN]:
            paddle2.move(5)

        ball.move()

        # Vérifier les collisions avec les raquettes
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        # Vérifier si la balle sort des limites et mettre à jour les scores
        if ball.rect.left <= 0:
            score2 += 1
            ball.rect.center = (largeur // 2, hauteur // 2)
            ball.speed_x *= -1
        if ball.rect.right >= largeur:
            score1 += 1
            ball.rect.center = (largeur // 2, hauteur // 2)
            ball.speed_x *= -1

        screen.fill(black)
        pygame.draw.rect(screen, white, paddle1.rect)
        pygame.draw.rect(screen, white, paddle2.rect)
        pygame.draw.ellipse(screen, white, ball.rect)
        pygame.draw.aaline(screen, white, (largeur// 2, 0), (largeur // 2, hauteur))

        # Afficher les scores
        text1 = font.render(str(score1), True, white)
        screen.blit(text1, (largeur // 4, 10))
        text2 = font.render(str(score2), True, white)
        screen.blit(text2, (largeur * 3 // 4, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= hauteur:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= largeur:
            self.speed_x *= -1
def main():
    # ... (le reste du code reste inchangé)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-5)
        if keys[pygame.K_s]:
            paddle1.move(5)
        if keys[pygame.K_UP]:
            paddle2.move(-5)
        if keys[pygame.K_DOWN]:
            paddle2.move(5)

        ball.move()

        # Vérifier les collisions avec les raquettes
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        # Vérifier si la balle sort des limites et mettre à jour les scores
        if ball.rect.left <= 0:
            score2 += 1
            ball.rect.center = (largeur // 2, hauteur // 2)
            ball.speed_x *= -1
        if ball.rect.right >= largeur:
            score1 += 1
            ball.rect.center = (largeur // 2, hauteur // 2)
            ball.speed_x *= -1

        screen.fill(black)
        pygame.draw.rect(screen, white, paddle1.rect)
        pygame.draw.rect(screen, white, paddle2.rect)
        pygame.draw.ellipse(screen, white, ball.rect)
        pygame.draw.aaline(screen, white, (hauteur // 2, 0), (largeur // 2, hauteur))

        # Afficher les scores
        text1 = font.render(str(score1), True, white)
        screen.blit(text1, (largeur // 4, 10))
        text2 = font.render(str(score2), True, white)
        screen.blit(text2, (largeur * 3 // 4, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
