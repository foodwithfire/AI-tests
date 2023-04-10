import pygame

window_size = (250, 400)
screen = pygame.display.set_mode(window_size)
scale = 50

cells = []
for y in range(int(window_size[1]/scale)):
    for x in range(int(window_size[0] / scale)):
        cells.append(0)

numbers_blueprint = {
    1: [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    2: [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    3: [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    4: [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    5: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    6: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    7: [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    8: [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    9: [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
}


def get_blueprint():
    blueprint = []
    for y in range(int(window_size[1] / scale)):
        for x in range(int(window_size[0] / scale)):
            if screen.get_at((x * scale, y * scale))[2] == 255:
                blueprint.append(1)
            else:
                blueprint.append(0)
    return blueprint


def compare_blueprints():
    scores = []
    for key in numbers_blueprint:
        score = 0
        blueprint = get_blueprint()
        idx = 0
        for number in numbers_blueprint[key]:
            score += int(number == blueprint[idx])
            idx += 1
        scores.append((key, score))

    sorted = False
    while not sorted:
        sorted = True
        idx = 0
        for i in range(len(scores) - 1):
            if scores[idx][1] < scores[idx + 1][1]:
                sorted = False
                temp = scores[idx]
                scores[idx] = scores[idx + 1]
                scores[idx + 1] = temp
            idx += 1

    return str(scores[0][0])


running = True
while running:
    cx, cy = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    idx = 0
    for y in range(int(window_size[1] / scale)):
        for x in range(int(window_size[0] / scale)):
            cell = pygame.Surface((scale, scale))
            if (int(cx / scale), int(cy / scale)) == (x, y) and mouse[0]:
                cells[idx] = 1
            c = cells[idx] * 255
            cell.fill((c, c, c))
            screen.blit(cell, (x * scale, y * scale))
            idx += 1

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print("You drew the number " + compare_blueprints() + ".")
