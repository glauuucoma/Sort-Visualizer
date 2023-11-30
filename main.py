import pygame
import random
import math
pygame.init()

class DrawInformation:
	
    # Color implementaton
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE
	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]
	
	#Font
	mediumFontSize = 18
	largeFontSize = 40
	FONT = pygame.font.Font(pygame.font.get_default_font(), mediumFontSize)
	LARGE_FONT = pygame.font.Font(pygame.font.get_default_font(), largeFontSize)
	
    #Paddings
	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
	# Fill background with grey color
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	# Display options
	controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
	draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 ,20))

	# Display available algorihms
	sorting = draw_info.FONT.render("I - Insertion sort | B - Bubble sort", 1, draw_info.BLACK)
	draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 ,55))

	# Update screen
	draw_list(draw_info)
	pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg = False):
	lst = draw_info.lst

	if clear_bg:
		clear_rect = (draw_info.SIDE_PAD //2, draw_info.TOP_PAD, 
				draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
		pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
		color = draw_info.GRADIENTS[i % 3] # Generate random color using modulo operator

		if i in color_positions:
			color = color_positions[i]

		pygame.draw.rect(draw_info.window, color, (x,y, draw_info.block_width, draw_info.height))
	
	if clear_bg:
		pygame.display.update()


def generate_starting_list(n, min_val, max_val):
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst

def bubble_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j] 
			num2 = lst[j+1]

			if num1 > num2 and ascending:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				draw_list(draw_info, {j:draw_info.GREEN, j + 1: draw_info.RED}, True)
				#draw_list()
				yield True
	
	return lst


def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInformation(800, 600, lst)
	ascending = True
	sorting = False

	sorting_algorithm = bubble_sort # Current algorithm used
	sorting_algo_name = "Bubble sort"
	sorting_algo_generator = None

	while run:
		clock.tick(60)
 
		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False
		else:
			draw(draw_info)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_r:
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting == False
			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			


		
	pygame.quit()


if __name__ == "__main__":
	main()
	