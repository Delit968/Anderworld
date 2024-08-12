import pygame
import webbrowser
import json
from constant import HEIGHT, WIDTH
from dop_class import Font_s, GameScreen, Protagonist

pygame.init()

class Game:
    def __init__(self) -> None:
        self.mode = 'Load'
        self.running = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.loading()
        self.screen_init()
        self.pl = Protagonist(736, 432, self.screen)
        self.run()

    def screen_init(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Тест 8")
        pygame.display.set_icon(pygame.image.load('img/settings_images/icon.ico'))

    def loading(self):
        DATA = {
            "name": "",
            "age": 0,
            "city": "",
            "items":0,
            "level": 0,
            "hp|at|mp|ex": "10|0-5|0|0",
            "s|l|i": "1|1|1",
            "last_save": ""
        }
        ALL = {
            "level": 0,
            "hp|at|mp|ex": "10|0-5|0|0",
            "last_save": ""
        }
        try:
            with open('settings.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                if "level" in data:
                    self.num_level = data["level"]
                    self.level = "LEVEL"+str(self.num_level)

                    if "level" in data:
                        self.num_item = data["level"]
                        self.item = "LEVEL"+str(self.num_level)

                    if "hp|at|mp|ex" in data:
                        save = data["hp|at|mp|ex"].split('|')
                        self.hp = save[0]
                        self.damage = save[1]
                        self.mana = save[2]
                        self.experience = save[3]
                    if "s|l|i" in data:
                        save1 = data["s|l|i"].split('|')
                        self.power = save1[0]
                        self.agility = save1[1]
                        self.intelligence = save1[2]
                    if "inventori" in data:
                        save1 = data["s|l|i"].split('|')
                        self.power = save1[0]
                        self.agility = save1[1]
                        self.intelligence = save1[2]

                else:
                    with open('settings.json', 'w', encoding='utf-8') as write_file:
                        json.dump(ALL, write_file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            with open('settings.json', 'w', encoding='utf-8') as file:
                json.dump(DATA, file, ensure_ascii=False, indent=4)
        print('Загрузка окончена')  # temp
        self.mode = 'Menu'
        
    def run(self):
        self.update()
        #self.sound()

    def update(self):
        game_screen = GameScreen()
        while self.running:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mode == 'Menu' and self.start_text_rect.collidepoint((self.mouse_x, self.mouse_y)):
                        self.mode = 'Game'
                    elif self.mode == 'Menu' and self.settings_text_rect.collidepoint((self.mouse_x, self.mouse_y)):
                        self.mode = 'Settings'
                    elif self.mode == 'Menu' and self.autor_text_rect.collidepoint((self.mouse_x, self.mouse_y)):
                        webbrowser.open('https://steamcommunity.com/profiles/76561199734640803/')
                elif self.mode == 'Game':
                    self.pl.move(event, game_screen.bricks, game_screen.items)

            self.screen.fill((0, 0, 0))
            self.logic()
            self.draw(game_screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
            
    def draw(self, game_screen):
        self.images_init()
        self.fonts_init()
        if self.mode == 'Menu':
            self.screen.blit(self.mouse, (self.mouse_x, self.mouse_y))
        elif self.mode == 'Game':
            game_screen.draw_all(self.level, self.screen, self.item)
            self.pl.draw()

    def images_init(self):
        background = pygame.image.load('img/settings_images/background1.png')
        self.scaled_image = pygame.transform.scale(background, (WIDTH, HEIGHT))
        self.mouse = pygame.image.load('img/settings_images/maus.png').convert_alpha()
    
    def fonts_init(self):
        if self.mode == 'Menu':
            self.start_text_rect = Font_s.draw('Старт', WIDTH / 2, HEIGHT / 2, self.screen)
            self.settings_text_rect = Font_s.draw('Настройки', WIDTH / 2 - 50, HEIGHT / 2 - 50, self.screen)
            self.autor_text_rect = Font_s.draw('Автор', WIDTH / 2 - 100, HEIGHT / 2 - 100, self.screen)
            self.thanks_text_rect = Font_s.draw('Я благодарен за поддержку моего продукта', WIDTH / 2 + 200, HEIGHT / 2 + 200, self.screen)
            self.thanks_text_rect = Font_s.draw('ANDERWORLD', 100, 100, self.screen)

    def logic(self):
        pygame.mouse.set_visible(False)
