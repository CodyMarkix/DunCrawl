import pygame
import pygame.font
import os
import time
import json

# Initiation
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Resolution, variable for the window and name of the game
WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DunCrawl")
pygame.mouse.set_visible(False)

# Hardcoded FPS
FPS = 60


# Game logic
def game():
	# Player info
	player_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'player.png'))
	plr_scaled = pygame.transform.rotate(pygame.transform.scale(player_img, (88, 98)), 0)
	player = pygame.Rect((639, 335), (88, 98))
	plr_vel = 5
	
	# Dungeon
	dungeon_img = pygame.image.load(os.path.join('Resources', 'images', 'map', 'dungeonchamber.png'))
	dungeon_scaled = pygame.transform.rotate(pygame.transform.scale(dungeon_img, (1366, 768)), 0)
	dungeon = pygame.Rect((0, 0), (1366, 768))

	# UI
	MinecraftTen = pygame.font.Font(os.path.join('Resources', 'fonts', 'MinecraftTen.ttf'), 32)
	
	Itemlist = MinecraftTen.render("Items:", True, (255, 255, 255), None)
	Itemframe1_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'itemframe.png'))
	Itemframe2_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'itemframe.png'))
	Itemframe3_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'itemframe.png'))
	Itemframe4_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'itemframe.png'))
	Itemframe1 = pygame.transform.rotate(pygame.transform.scale(Itemframe1_img, (74, 74)), 0)
	Itemframe2 = pygame.transform.rotate(pygame.transform.scale(Itemframe2_img, (74, 74)), 0)
	Itemframe3 = pygame.transform.rotate(pygame.transform.scale(Itemframe3_img, (74, 74)), 0)
	Itemframe4 = pygame.transform.rotate(pygame.transform.scale(Itemframe4_img, (74, 74)), 0)

	HP_sign = MinecraftTen.render("Health:", True, (255, 255, 255), None)
	heart_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'heart.png'))
	lost_heart_img = pygame.image.load(os.path.join('Resources', 'images', 'player', 'heart_lost.png'))
	heart = pygame.transform.rotate(pygame.transform.scale(heart_img, (64, 64)), 0)
	lost_heart = pygame.transform.rotate(pygame.transform.scale(heart_img, (64, 64)), 0)


	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_ESCAPE]:
			return	

		if keys_pressed[pygame.K_w] and player.y - plr_vel > 250:
			player.y -= plr_vel

		if keys_pressed[pygame.K_s] and player.y + plr_vel + 98 < 639:
			player.y += plr_vel

		if keys_pressed[pygame.K_d] and player.x + plr_vel < 1140:
			player.x += plr_vel

		if keys_pressed[pygame.K_a] and player.x - plr_vel > 140:
			player.x -= plr_vel

		# Drawing sprites
		def draw_window():
			# Declaring colors/sprites
			BG = (20, 25, 20)
			WIN.fill(BG)
			WIN.blit(dungeon_scaled	, (dungeon.x, dungeon.y))
			WIN.blit(plr_scaled, (player.x, player.y))
			
			WIN.blit(Itemlist, (800, 10))
			WIN.blit(Itemframe1, (800, 40))
			WIN.blit(Itemframe2, (884, 40))
			WIN.blit(Itemframe3, (968, 40))
			WIN.blit(Itemframe4, (1052, 40))

			WIN.blit(HP_sign, (100, 10))
			WIN.blit(heart, (100, 40))
			WIN.blit(heart, (174, 40))
			WIN.blit(heart, (248, 40))
			WIN.blit(heart, (322, 40))
			WIN.blit(heart, (396, 40))
			pygame.display.update()	

		draw_window()

	pygame.quit()

def credits():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# Menu keys
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_ESCAPE]:
			main_menu()
		
		# Drawing sprites
		def draw_window():
			# Declaring colors/images
			M_BG = (20, 25, 20)
			WIN.fill(M_BG)
			CREDITS = pygame.image.load(os.path.join('Resources', 'images', 'menu', 'credits.png'))
			WIN.blit(CREDITS, (0, 0))
			pygame.display.update()
	
		draw_window()

	pygame.quit()


# Main menu logic
def main_menu():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		
		# Menu keys
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_e]:
			WIN.fill((0, 0, 0))
			pygame.display.update()
			
			pygame.mixer.music.load(os.path.join('Resources', 'sounds', 'menuselect.wav'))
			pygame.mixer.music.play(loops=1, start=0.0, fade_ms=0)	
			
			time.sleep(1.5)		
			run = False
		if keys_pressed[pygame.K_s]:
			pygame.mixer.music.load(os.path.join('Resources', 'sounds', 'startgame.wav'))
			pygame.mixer.music.play(loops=1, start=0.0, fade_ms=0)	
			time.sleep(0.5)
			game()

		if keys_pressed[pygame.K_c]:
			pygame.mixer.music.load(os.path.join('Resources', 'sounds', 'creditsselect.wav'))
			pygame.mixer.music.play(loops=1, start=0.0, fade_ms=0)
			credits()

		
		# Drawing sprites
		def draw_window():
			# Declaring colors/images
			M_BG = (20, 25, 20)
			LOGO = pygame.image.load(os.path.join('Resources', 'images', 'menu', 'logo.png'))
			QUITGAME = pygame.image.load(os.path.join('Resources', 'images', 'menu', 'gamequit.png'))
			STARTGAME = pygame.image.load(os.path.join('Resources', 'images', 'menu', 'gamestart.png'))
			CREDITS = pygame.image.load(os.path.join('Resources', 'images', 'menu', 'creditsselect.png'))
			
			# Actually drawing
			WIN.fill(M_BG)
			WIN.blit(LOGO, (363, 150))
			WIN.blit(STARTGAME, (303, 400))
			WIN.blit(QUITGAME, (353, 520))
			WIN.blit(CREDITS, (253, 650))

			pygame.display.update()
	
		draw_window()

	pygame.quit()

main_menu()