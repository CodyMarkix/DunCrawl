import pygame
import os
import time

# Initiation
pygame.init()
pygame.mixer.init()

# Resolution, variable for the window and name of the game
WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DunCrawl")

# Hardcoded FPS
FPS = 60

# Game logic

def game():
	player_img = pygame.image.load(os.path.join('Resources', 'images', 'player.png'))
	plr_scaled = pygame.transform.rotate(pygame.transform.scale(player_img, (88, 98)), 0)
	player = pygame.Rect((100, 100), (88, 98))
	plr_vel = 5
	
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_ESCAPE]:
			run = False

		if keys_pressed[pygame.K_w]:
			player.y -= plr_vel

		if keys_pressed[pygame.K_s]:
			player.y += plr_vel

		if keys_pressed[pygame.K_d]:
			player.x += plr_vel
		
		if keys_pressed[pygame.K_a]:
			player.x -= plr_vel

		# Drawing sprites
		def draw_window():
			# Declaring colors/sprites
			BG = (20, 25, 20)
			WIN.fill(BG)
			WIN.blit(plr_scaled, (player.x, player.y))
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
			time.sleep(0.5)
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