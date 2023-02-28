import os
import sys  
from pathlib import Path
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import pygame
pygame.font.init()
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
font_path_1 = os.path.join(root_dir, "fonts", "Arista20AlternateRegular-jy89.ttf")
font_path_2 = os.path.join(root_dir, "fonts", "PartyConfettiRegular-eZOn3.ttf")
font_path_3 = os.path.join(root_dir, "fonts", "GoldleafBoldPersonalUseBold-eZ4dO.ttf")

back_color_pallet = {
    'screen_back': (249, 249, 249),
    'back': (207, 230, 223),
    'back_tile': (186, 217, 217),
    'button_top': (144, 149, 158),
    'button_bottom': (72, 70, 102),
    'yellow_top': (255, 204, 102),
    'yellow_bottom':(194, 162, 97),
    'black_bottom': (0,0,0),
    1: (102, 204, 255),
    '1_back': (95,169,241),
    2: (255, 102, 128),
    '2_back': (204,82,122),
    3: (253, 255, 255),
    '3_back': (255,204,102),
    6: (253, 255, 255),
    '6_back': (255,204,102),
    12: (253, 255, 255),
    '12_back': (255,204,102),
    24: (253, 255, 255),
    '24_back': (255,204,102),
    48: (253, 255, 255),
    '48_back': (255,204,102),
    96: (253, 255, 255),
    '96_back': (255,204,102),
    192: (253, 255, 255),
    '192_back': (255,204,102),
    384: (253, 255, 255),
    '384_back': (255,204,102),
    768: (253, 255, 255),
    '768_back': (255,204,102),
    1536: (253, 255, 255),
    '1536_back': (255,204,102),
    3072: (253, 255, 255),
    '3072_back': (255,204,102),
    6144: (253, 255, 255),
    '6144_back': (255,204,102)
}

number_color_pallet = {
    'title_1': (144, 149, 158),
    'title_2': (255, 102, 128),
    'title_3': (102, 204, 255),
    'text_1': (144, 149, 158),
    'text_2': (0, 0, 0),
    'max_number': (255, 102, 128),
    1: (255, 255, 255),
    2: (255, 255, 255),
    3: (0, 0, 0),
    6: (0, 0, 0),
    12: (0, 0, 0),
    24: (0, 0, 0),
    48: (0, 0, 0),
    96: (0, 0, 0),
    192: (0, 0, 0),
    384: (0, 0, 0),
    768: (0, 0, 0),
    1536: (0, 0, 0),
    3072: (0, 0, 0),
    6144: (255, 102, 128)
}

usual_fonts = {
    'title_game': pygame.font.Font(font_path_2, 70),
    'text_init_screen': pygame.font.SysFont('impact', 15),
    'title_game_over': pygame.font.Font(font_path_2, 70),
    'title_ranking': pygame.font.Font(font_path_2, 40),
    'text_game_over_screen': pygame.font.SysFont('impact', 15)
}


