import pygame  # Импортируем библиотеку Pygame
import win32api  # Импортируем библиотеку для работы с Windows API
import win32con  # Импортируем библиотеку для работы с константами Windows API
import win32gui  # Импортируем библиотеку для работы с графическими окнами Windows API

# Считываем размеры экрана 
width = win32api.GetSystemMetrics(0)  # Получаем ширину экрана
height = win32api.GetSystemMetrics(1)  # Получаем высоту экрана
print(width, height)  # Выводим размеры экрана в консоль

# Загружаем изображение иконки
programIcon = pygame.image.load('icon/icon_vunc.png')  # Загружаем изображение иконки из файла

pygame.init()  # Инициализируем библиотеку Pygame

# Создаем окно
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)  # Создаем окно с размерами width и height, а также без рамки
pygame.display.set_icon(programIcon)  # Устанавливаем иконку для окна
done = False  # Определяем переменную done инициализированную в значение False

# Определяем цвет фона
fuchsia = (255, 0, 128)  

# Загружаем изображение
image = pygame.image.load("image/MissionPlaner.png").convert_alpha()  # Загружаем изображение из файла и преобразуем его в альфа-канал

# Получаем идентификатор окна
hwnd = pygame.display.get_wm_info()["window"]  # Получаем идентификатор окна с помощью функции get_wm_info()

# Устанавливаем стиль окна
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# Устанавливаем атрибуты слоя окна
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

# Устанавливаем позицию окна
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Основной цикл программы
while not done:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Если событие - закрытие окна
            done = True  # Устанавливаем переменную done в значение True

    screen.fill(fuchsia)  # Заливаем экран цветом фона
    screen.blit(image, (0, 0))  # Отображаем изображение на экране
    pygame.display.update()  # Обновляем экран



