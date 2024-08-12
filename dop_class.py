import pygame
import importlib
import random

class Font_s:
    def __init__(self):#для диалогов
        pass

    @staticmethod
    def draw(text, x, y, screen):
        font = pygame.font.Font('fonts/Sans_Font.ttf', 30)
        form = font.render(text, True, (255, 255, 255))
        form_rect = form.get_rect(center=(x, y))
        screen.blit(form, form_rect)
        return form_rect


class GameScreen:
    def __init__(self):
        self.init_images()
        self.bricks = []
        self.items = []

    def draw_all(self, level, screen,item):
        self.draw_cells(level, screen)
        self.draw_items(item,screen)

    def init_images(self):
        self.image_bigbricks = pygame.image.load('img/img_with_tiles/Bigbricks.png')
        self.image_grass = pygame.image.load('img/img_with_tiles/Grass.png')
        self.image_item1 = pygame.image.load('img\img_with_items\WidePotion-outline1.png')

    def draw_cells(self, level_name, screen):
        self.bricks = []
        brick_width = self.image_bigbricks.get_width()
        brick_height = self.image_bigbricks.get_height()
        levels_module = importlib.import_module('levels')
        level = getattr(levels_module, level_name)
        screen_width, screen_height = screen.get_size()
        left_offset = (screen_width - (brick_width * 30)) // 2 # 720
        top_offset = (screen_height - (brick_height * 16)) // 2 # 412
        for i in range(len(level)):
            for j in range(len(level[0])):
                left = left_offset + brick_width * j
                top = top_offset + brick_height * i
                if level[i][j] == 0:
                    screen.blit(self.image_bigbricks, (left, top))
                    self.bricks.append(pygame.Rect(left, top, brick_width, brick_height))
                elif level[i][j] == 1:
                    screen.blit(self.image_grass, (left, top))       
                
    def draw_items(self, level_name, screen):
        self.items = []
        brick_width = self.image_bigbricks.get_width()
        brick_height = self.image_bigbricks.get_height()
        levels_module = importlib.import_module('items')
        level = getattr(levels_module, level_name)
        screen_width, screen_height = screen.get_size()
        left_offset = (screen_width - (brick_width * 30)) // 2
        top_offset = (screen_height - (brick_height * 16)) // 2 
        for i in range(len(level)):
            for j in range(len(level[0])):
                left = left_offset + brick_width * j
                top = top_offset + brick_height * i
                if level[i][j] == 1:
                    screen.blit(self.image_item1, (left, top))
                    self.items.append(pygame.Rect(left, top, brick_width, brick_height))
            
class Protagonist:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('img/settings_images/HalfHumanRanger1.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.inventory = []

    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)

    def move(self, event, bricks, items):
        if event.type == pygame.KEYDOWN:
            new_rect = self.rect.copy()
            if event.key == pygame.K_w:
                new_rect.y -= 16 
            elif event.key == pygame.K_a:
                new_rect.x -= 16
            elif event.key == pygame.K_s:
                new_rect.y += 16  
            elif event.key == pygame.K_d:
                new_rect.x += 16
            
            if not any(new_rect.colliderect(brick) for brick in bricks):
                self.rect = new_rect

            for item in items[:]:  # чтобы не забыл это для списка который меняеться во время интерациий
                if new_rect.colliderect(item):
                    self.inventory.append(item)
                    items.remove(item)  
                    print("Предмет собран!")

class Item:
    def __init__(self,rare_experience,rare_hp,rare_mana,legendary_power) -> None:
        self.rare_hp = rare_hp
        self.rare_experience = rare_experience
        self.rare_mana = rare_mana
        self.hp = random.randint(0,rare_hp)
        self.mana = random.randint(0,rare_mana)
        self.experience = random.randint(0,rare_experience)
        self.power = random.randint(0,legendary_power)

