import pygame
from ui.ui_container import UIContainer
from ui.math import vec2

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

class UISystem:
    def __init__(self):
        self.containers = []

    def add_container(self, container: UIContainer):
        self.containers.append(container)

    def handle_events(self):
        for event in pygame.event.get():
            for ctr in self.containers:
                ctr.handle_event(event)

    def update(self):
        for ctr in self.containers:
            ctr.render(screen)
            ctr.update()
    
ctr1 = UIContainer("Hello", vec2(0, 0), 100, 500)
ctr1.add_button(False, "Hello", False)

ctr2 = UIContainer("Bye", vec2(100, 0), 100, 500)
ctr2.add_label("Bye")
ctr2.add_number(0, "BYEBYE")

ui_system = UISystem()
ui_system.add_container(ctr1)
ui_system.add_container(ctr2)

while True:
    ui_system.handle_events()

    screen.fill("black")

    ui_system.update()

    pygame.display.flip()
    clock.tick(60)