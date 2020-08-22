import pygame, os
pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
pygame.joystick.init

joystick_count = pygame.joystick.get_count()

Running = True
while Running:
    clock.tick(40)
    os.system("cls")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        axes = joystick.get_numaxes()
        buttons = joystick.get_numbuttons()

        for i in range(axes):
            axis = (joystick.get_axis(i) + 1.0) / 2.0
            print(F"Axis: {i} value: {axis}")

        for i in range(buttons):
            button = joystick.get_button(i)
            print(F"Button: {i} value: {button}")
        