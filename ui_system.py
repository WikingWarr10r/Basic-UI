import pygame
from ui.ui_container import UIContainer
from ui.math import vec2
from ui.pointer import Ptr

class UISystem:
    def __init__(self, screen):
        self.containers = []
        self.screen = screen

    def add_container(self, container: UIContainer):
        self.containers.append(container)

    def handle_events(self):
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                pygame.quit()
            for ctr in self.containers:
                ctr.handle_event(event)

    def update(self):
        for ctr in self.containers:
            ctr.render(self.screen)
            ctr.update()

if __name__ == "main.py":
    pygame.init()

    screen = pygame.display.set_mode((1280,720))

    clock = pygame.time.Clock()

    test_num = Ptr(0)
    test_bool = Ptr(False)

    container = UIContainer("Test", vec2(0, 0), 100, 500)
    container.add_number(0, "Test Num")
    container.add_button(False, "Test Button", True)
    container.link_value("Test Num", test_num)
    container.link_value("Test Button", test_bool)

    ui_system = UISystem(screen)
    ui_system.add_container(container)

    while True:
        ui_system.handle_events()

        screen.fill("black")

        print(test_num)
        print(test_bool)

        ui_system.update()

        pygame.display.flip()
        clock.tick(60)