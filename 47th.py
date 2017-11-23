# -*- coding:utf-8 -*-

import pygame

def main():
	screen = pygame.display.set_mode((480, 700), 0, 32)

	background = pygame.image.load("./001.png")

	while True:
		screen.blit(background, (0, 0))
		pygame.display.update()


if __name__ == '__main__':
	main()
