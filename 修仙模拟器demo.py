import pygame
import sys
import easygui

def print_box(surface, font, text, y_offset=0):
    box_width = len(max(text.split('\n'), key=len)) * 20
    box_height = len(text.split('\n')) * 30
    border = pygame.Surface((box_width, box_height))
    border.fill((255, 255, 255))

    for i, line in enumerate(text.split('\n')):
        text_surface = font.render(line, True, (0, 0, 0))
        x = (box_width - text_surface.get_width()) // 2
        y = i * 30
        border.blit(text_surface, (x, y))

    x_offset = (screen_width - box_width) // 2
    y_offset += (screen_height - box_height) // 2
    surface.blit(border, (x_offset, y_offset))

def draw_button(surface, rect, text):
    pygame.draw.rect(surface, (200, 200, 200), rect)
    font = pygame.font.SysFont('SimSun', 20)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("修仙模拟器Demo")

# Use a built-in font that supports Chinese characters
chinese_font = pygame.font.SysFont('SimSun', 20)

# Your game introduction text for different states
intro_texts = [
    "《修仙模拟器》——Test版\n修仙之途，生死轮回\n不问过往，追寻永恒"
]
# Create a font for the "Press any key to continue" message
continue_font = pygame.font.SysFont('Arial', 16)

# Initialize game state
current_state = 0

face, strong, iq, home = 0, 0, 0, 0  # Initial attribute values
total_points = 20

font = pygame.font.SysFont('SimSun', 20)

input_texts = [
    f"请输入颜值属性点数(1-10)",
    f"请输入体质属性点数(1-10)",
    f"请输入智力属性点数(1-10)",
    f"请输入家境属性点数(1-10)"
]

start_button = pygame.Rect(400, 400, 100, 40)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            current_state += 1

    # Clear the screen
    screen.fill((255, 255, 255))

    if current_state < len(intro_texts):
        # Draw the introduction text in a box, centered
        print_box(screen, chinese_font, intro_texts[current_state], y_offset=-50)

        # Draw the "Press any key to continue" message, centered
        continue_text = continue_font.render("Press any key to continue...", True, (0, 0, 0))
        screen.blit(continue_text, ((screen_width - continue_text.get_width()) // 2, screen_height - 50))
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        # Check if the user clicked on buttons to adjust attributes
        if mouse_buttons[0] and not prev_mouse_pressed:  # Check if the left mouse button is pressed
            if 360 <= mouse_x <= 390 and 150 <= mouse_y <= 180:
                face = max(1, face - 1)
            elif 440 <= mouse_x <= 470 and 150 <= mouse_y <= 180:
                face = min(10, face + 1)

            if 360 <= mouse_x <= 390 and 200 <= mouse_y <= 230:
                strong = max(1, strong - 1)
            elif 440 <= mouse_x <= 470 and 200 <= mouse_y <= 230:
                strong = min(10, strong + 1)

            if 360 <= mouse_x <= 390 and 250 <= mouse_y <= 280:
                iq = max(1, iq - 1)
            elif 440 <= mouse_x <= 470 and 250 <= mouse_y <= 280:
                iq = min(10, iq + 1)

            if 360 <= mouse_x <= 390 and 300 <= mouse_y <= 330:
                home = max(1, home - 1)
            elif 440 <= mouse_x <= 470 and 300 <= mouse_y <= 330:
                home = min(10, home + 1)

            # Check if the total points are valid before starting the journey
            if 350 <= mouse_x <= 450 and 400 <= mouse_y <= 440:
                if face + strong + iq + home == total_points:
                    print(f"颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}")
                    running = False
                else:
                    easygui.msgbox("属性点总数不等于20，请重新调整。", "提示")
       
        prev_mouse_pressed = mouse_buttons[0]
        
        # Draw buttons for all attributes
        draw_button(screen, pygame.Rect(360, 150, 30, 30), "[-]")
        draw_button(screen, pygame.Rect(400, 150, 30, 30), f"[{face}]")
        draw_button(screen, pygame.Rect(440, 150, 30, 30), "[+]")
        draw_button(screen, pygame.Rect(360, 200, 30, 30), "[-]")
        draw_button(screen, pygame.Rect(400, 200, 30, 30), f"[{strong}]")
        draw_button(screen, pygame.Rect(440, 200, 30, 30), "[+]")
        draw_button(screen, pygame.Rect(360, 250, 30, 30), "[-]")
        draw_button(screen, pygame.Rect(400, 250, 30, 30), f"[{iq}]")
        draw_button(screen, pygame.Rect(440, 250, 30, 30), "[+]")
        draw_button(screen, pygame.Rect(360, 300, 30, 30), "[-]")
        draw_button(screen, pygame.Rect(400, 300, 30, 30), f"[{home}]")
        draw_button(screen, pygame.Rect(440, 300, 30, 30), "[+]")

        draw_button(screen, pygame.Rect(350, 400, 100, 40), "开始修仙")

        for i, text in enumerate(input_texts):
            input_rect = pygame.Rect(50, 150 + i * 50, 300, 40)
            pygame.draw.rect(screen, (200, 200, 200), input_rect)
            pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
            input_surface = font.render(text, True, (0, 0, 0))
            screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))
    
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

