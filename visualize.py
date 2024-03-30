from src.context import SortContext
from src.strategy import SortType
from src.utils import Utils
import pygame

if __name__ == "__main__":
    pygame.init()

    sort_type = SortType.SELECTION
    data = Utils.generate_random_list(50)
    sort = SortContext(data, sort_type)

    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(f"Sorting Algorithm Visualizer {sort_type}")
    x, y = 40, 40
    width = 5
    padding = 2

    def show(data: list[int]) -> None:
        for i in range(len(data)):
            pygame.draw.rect(
                win,
                (0, 0, 0),
                (x + i * (width + padding), y, width, data[i]),
            )

    run = True
    while run:
        pygame.time.delay(1)
        execute = False
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_SPACE]:
            execute = True

        if not execute:
            win.fill((0, 0, 0))
            show(data)
            pygame.display.update()
        else:
            for i in range(len(data) - 1):
                for j in range(len(data) - i - 1):
                    if data[j] > data[j + 1]:
                        t = data[j]
                        data[j] = data[j + 1]
                        data[j + 1] = t

                    win.fill((0, 0, 0))
                    show(data)
                    pygame.time.delay(10)
                    pygame.display.update()

    pygame.quit()
