import pygame as pg
import pygame_gui
import constants as c
import Organism

def main():
    pg.init()
    screen = pg.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
    pg.display.set_caption("2D World Simulator")
    icon = pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Earth.png")
    pg.display.set_icon(icon)
    manager = pygame_gui.UIManager((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))

    label_rect = pg.Rect(0, 0, 200, c.DROPDOWN_MENU_HEIGHT)  # Position and size of the label
    label_element = pygame_gui.elements.UILabel(
        relative_rect=label_rect,
        text="Selected Organism:",  # Label text
        manager=manager
    )

    dropdown_menu = pygame_gui.elements.UIDropDownMenu(
        Organism.organisms[1:],
        "Antelope",
        pg.Rect(200, 0, 200, c.DROPDOWN_MENU_HEIGHT),
        manager=manager
    )

    empty_tile = pg.Surface((c.TILE_SIZE, c.TILE_SIZE))
    empty_tile.fill(c.GRASS_GREEN)
    
    icons = [
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Human.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Wolf.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Sheep.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Antelope.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Fox.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Turtle.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Grass.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/SowThistle.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Guarana.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Belladonna.png")), (c.TILE_SIZE, c.TILE_SIZE)),
        pg.transform.scale((pg.image.load("C:/Users/wikto/Desktop/Studia/sem2/oop/2D_World_Simulator/py/icons/Hogweed.png")), (c.TILE_SIZE, c.TILE_SIZE)),
    ]

    chosen_organism = icons[Organism.OrganismType.ANTELOPE.value]

    tiles = []
    for y in range(int(c.BOARD_HEIGHT/c.TILE_SIZE)):
        row = []
        for x in range(int(c.BOARD_WIDTH/c.TILE_SIZE)):
            row.append([empty_tile, [x*c.TILE_SIZE, y*c.TILE_SIZE]])
        tiles.append(row)

    selected_tile = None

    clock = pg.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                adjusted_pos = (event.pos[0], event.pos[1] - c.DROPDOWN_MENU_HEIGHT)
                x = adjusted_pos[0] // c.TILE_SIZE
                y = adjusted_pos[1] // c.TILE_SIZE
                selected_tile = (x, y)
                if event.button == c.LEFT_MOUSE_BUTTON:
                    if(y >= 0 and y < int(c.BOARD_HEIGHT/c.TILE_SIZE) and x >= 0 and x < int(c.BOARD_WIDTH/c.TILE_SIZE)):
                        tiles[y][x][0] = empty_tile
                elif event.button == c.RIGHT_MOUSE_BUTTON:
                    if(y >= 0 and y < int(c.BOARD_HEIGHT/c.TILE_SIZE) and x >= 0 and x < int(c.BOARD_WIDTH/c.TILE_SIZE)):
                        tiles[y][x][0] = chosen_organism
            elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == dropdown_menu:
                    selected_organism = event.text
                    chosen_organism = icons[Organism.organism_types[selected_organism].value]
            manager.process_events(event)

        manager.update(time_delta)

        screen.fill(c.WHITE)

        for row in tiles:
            for img, pos in row:
                screen.blit(img, (pos[0], pos[1] + c.DROPDOWN_MENU_HEIGHT))

        drawGrid(screen, (0, c.DROPDOWN_MENU_HEIGHT))
        manager.draw_ui(screen)

        pg.display.update()

    pg.quit()

def drawGrid(screen, start_pos):
    rows = c.WINDOW_HEIGHT // c.TILE_SIZE
    cols = c.WINDOW_WIDTH // c.TILE_SIZE
    for x in range(cols):
        for y in range(rows):
            rect = pg.Rect(
                start_pos[0] + x * c.TILE_SIZE,
                start_pos[1] + y * c.TILE_SIZE,
                c.TILE_SIZE,
                c.TILE_SIZE
            )
            pg.draw.rect(screen, c.BLACK, rect, 1)

if __name__ == "__main__":
    main()