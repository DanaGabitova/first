import pygame

if __name__ == '__main__':
    try:
        width = int(input())
        height = int(input())
        pygame.init()
        size = width, height
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Крест")
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)
        pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), width=5)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.update()
        pygame.quit()
    except ValueError:
        print("Неправильный формат ввода")
