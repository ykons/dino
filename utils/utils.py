import os, random
import pygame

import utils.values as vl


def extractDigits(number):
    if number > -1:
        digits = []
        while(int(number/10) != 0):
            digits.append(number % 10)
            number = int(number/10)

        digits.append(number % 10)
        for _ in range(len(digits), 5):
            digits.append(0)
        digits.reverse()
        return digits


def load_image(name, x, y, width, height, scalex=-1, scaley=-1, colorkey=None):

    fullname = os.path.join(vl.SPRITE_PATH, name)
    sprite = pygame.image.load(fullname)
    sprite = sprite.convert()

    rect = pygame.Rect((x, y, width, height))
    image = pygame.Surface(rect.size)

    image = image.convert()
    image.blit(sprite, (0, 0), rect)

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image, (scalex, scaley))

    return (image, image.get_rect())


def load_sprite_sheet(sheetname, x, y, width, height, nx, ny, scalex=-1, scaley=-1, colorkey=None):

    fullname = os.path.join(vl.SPRITE_PATH, sheetname)
    sprite = pygame.image.load(fullname)
    sprite = sprite.convert()

    rect = pygame.Rect((x, y, width, height))
    sheet = pygame.Surface(rect.size)

    sheet = sheet.convert()
    sheet.blit(sprite, (0, 0), rect)

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0, ny):
        for j in range(0, nx):
            rect = pygame.Rect((j*sizex, i*sizey, sizex, sizey))
            image = pygame.Surface(rect.size)

            image = image.convert()
            image.blit(sheet, (0, 0), rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey, pygame.RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image, (scalex, scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites, sprite_rect


def replaceColorSprints(spints, colorOld, colorNew):
    for surface in spints:
        replaceColor(surface, colorOld, colorNew)


def replaceColor(surface, colorOld, colorNew):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = colorNew
    for x in range(w):
        for y in range(h):
            cor = surface.get_at((x, y))
            if((cor[0:3] == colorOld[0:3])):
                surface.set_at((x, y), pygame.Color(r, g, b, cor[3]))


def random_color():
    rgbl = [random.randint(200, 255), 0, 0]
    random.shuffle(rgbl)
    return tuple(rgbl)
