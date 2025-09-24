import random
import pygame

pygame.init()

# Colors
bar_color = (255,80, 0)
back_color = (50, 50, 50)
switch_color = (255, 255, 255)

# Dimensions
screen_height = 500
screen_width = 500
num_bars = int(input("how many random values do you want to sort through?: "))
rec_width=screen_width//num_bars


#Speed setting
tick = int(input("How mant fps do you want? "))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Visual Bubble Sort")
clock = pygame.time.Clock()

# Generate bars
def generate_bars():
    bars = []
    for _ in range(num_bars):
        bars.append(random.randint(10, screen_height))
    return bars

bars = generate_bars()

# Bubble sort indices
i = 0  # outer loop
j = 0  # inner loop
sorting = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(back_color)

    # Draw bars
    for idx in range(len(bars)):
        bar_height = bars[idx]

        # Highlight the bars currently being compared
        if idx == j or idx == j + 1:
            color = switch_color
        else:
            color = bar_color

        x = idx * rec_width
        y = screen_height - bar_height
        pygame.draw.rect(screen, color, (x, y, rec_width, bar_height))

    # Bubble sort step
    if sorting:
        if i < len(bars):
            if j < len(bars) - i - 1:
                if bars[j] > bars[j + 1]:
                    temp = bars[j]
                    bars[j] = bars[j + 1]
                    bars[j + 1] = temp
                j += 1
            else:
                j = 0
                i += 1
        else:
            sorting = False  # Done sorting

    pygame.display.flip()
    clock.tick(tick)  # Slow down for visualization

pygame.quit()
