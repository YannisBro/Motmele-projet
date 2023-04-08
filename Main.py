import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de mot mêlé")

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Définition des polices de caractères
font = pygame.font.SysFont(None, 36)

# Définition des mots à mélanger
WORDS = ["PYGAME", "ORDINATEUR", "CLAVIER", "SOURIS", "ECRAN", "FENETRE", "CODE", "PROGRAMMATION", "PYTHON", "DEVELOPPEMENT", "ALGORITHME", "VARIABLE", "BOUCLE", "CONDITION"]

# Fonction pour dessiner le bouton "Rejouer"
def draw_restart_button():
    pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH/4, SCREEN_HEIGHT*3/4, SCREEN_WIDTH/2, 50))
    text = font.render("Rejouer", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4 + 25))
    screen.blit(text, text_rect)

# Fonction pour recommencer le jeu
def restart_game():
    global word, mixed_word, guess, game_over
    word = random.choice(WORDS)
    mixed_word = list(word)
    random.shuffle(mixed_word)
    mixed_word = ''.join(mixed_word)
    guess = ""
    game_over = False

# Choix aléatoire du mot à deviner
word = random.choice(WORDS)

# Mélange des lettres du mot à deviner
mixed_word = list(word)
random.shuffle(mixed_word)
mixed_word = ''.join(mixed_word)

# Variables de jeu
guess = ""
game_over = False
score = 0

# Boucle de jeu
running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    guess += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                elif event.key == pygame.K_RETURN:
                    if guess.lower() == word.lower():
                        score += 1
                        game_over = True
                    else:
                        guess = ""
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if SCREEN_WIDTH/4 <= event.pos[0] <= SCREEN_WIDTH*3/4 and SCREEN_HEIGHT*3/4 <= event.pos[1] <= SCREEN_HEIGHT*3/4 + 50:
                    restart_game()
                    score = 0

    # Effacement de l'écran
    screen.fill(WHITE)

    # Affichage du mot à deviner
    text = font.render("Trouvez le mot : " + mixed_word, True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(text, text_rect)

    # Affichage de la saisie du joueur
   
     
    text = font.render(guess.upper(), True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)

    # Affichage du résultat de la devinette
    if game_over:
        if guess.lower() == word.lower():
            text = font.render("Bravo, vous avez trouvé !", True, GREEN)
            draw_restart_button()
        else:
            text = font.render("Dommage, le mot était " + word, True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4))
        screen.blit(text, text_rect)

    # Mise à jour de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()


