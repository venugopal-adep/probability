import pygame
import sys
import math
from scipy.stats import binom
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binomial Distribution Simulator")

# Font
font = pygame.font.Font(None, 32)

# Binomial Distribution parameters
n = 10
p = 0.5
x = 5

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_bar_chart(n, p, x):
    x_range = np.arange(n + 1)
    y = binom.pmf(x_range, n, p)
    max_y = max(y)
    bar_width = WIDTH // (n + 3)
    
    for i, prob in enumerate(y):
        bar_height = int(prob / max_y * 400)
        bar_x = (i + 1) * bar_width
        pygame.draw.rect(screen, LIGHT_BLUE, (bar_x, HEIGHT - 100 - bar_height, bar_width - 5, bar_height))
        pygame.draw.rect(screen, BLACK, (bar_x, HEIGHT - 100 - bar_height, bar_width - 5, bar_height), 1)
        
        if i == x:
            pygame.draw.rect(screen, RED, (bar_x, HEIGHT - 100 - bar_height, bar_width - 5, bar_height), 3)
        
        draw_text(str(i), bar_x + bar_width // 2 - 10, HEIGHT - 90)

    draw_text("Number of Successes", WIDTH // 2 - 100, HEIGHT - 50)

def main():
    global n, p, x
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and n < 20:
                    n += 1
                elif event.key == pygame.K_DOWN and n > 1:
                    n -= 1
                elif event.key == pygame.K_RIGHT and p < 1:
                    p = round(p + 0.1, 1)
                elif event.key == pygame.K_LEFT and p > 0:
                    p = round(p - 0.1, 1)
                elif event.key == pygame.K_w and x < n:
                    x += 1
                elif event.key == pygame.K_s and x > 0:
                    x -= 1

        screen.fill(WHITE)

        # Draw title
        draw_text("Binomial Distribution Simulator", 20, 20, BLUE)

        # Draw parameters
        draw_text(f"n (trials): {n} (↑↓)", 20, 60)
        draw_text(f"p (probability): {p:.1f} (←→)", 20, 90)
        draw_text(f"x (successes): {x} (W/S)", 20, 120)

        # Draw probability
        prob = binom.pmf(x, n, p)
        draw_text(f"P(X = {x}) = {prob:.4f}", 20, 150, RED)

        # Draw bar chart
        draw_bar_chart(n, p, x)

        pygame.display.flip()

if __name__ == "__main__":
    main()