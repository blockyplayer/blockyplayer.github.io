from ascii_magic import AsciiArt # type: ignore
from PIL import ImageEnhance

my_art = AsciiArt.from_image('lion.jpg')
my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
my_art.to_terminal()