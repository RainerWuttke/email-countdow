from PIL import Image, ImageFont, ImageDraw
from datetime import datetime, timedelta
import os
import requests
from io import BytesIO

# TODO Pegar dados dos parâmetros   
final_date = '2024-12-16 20:00'
font_family = ''
font_color = '#fff'
background_color = '#BA7D63'
background_image_url = ''
fontMarginOffset = 15
font_size = 35
boxSizes = [
    {
        "boxStart": {"x":330, "y":50}, 
        "boxEnd": {"x":385, "y":125}
    }, 
    {
        "boxStart": {"x":395, "y":50}, 
        "boxEnd": {"x":445, "y":125}
    }, 
    {
        "boxStart": {"x":460, "y":50}, 
        "boxEnd": {"x":505, "y":125}
    }, 
    {
        "boxStart": {"x":520, "y":50}, 
        "boxEnd": {"x":570, "y":125}
    }
]

seconds_to_count = 240  # Número de frames (segundos) que serão gerados

def calculate_time_remaining(final_date, current_date):
    """
    Calcula a diferença de tempo entre duas datas.
    :param final_date: Data final como objeto datetime
    :param current_date: Data atual como objeto datetime
    :return: String (DD HH:mm:SS)
    """
    time_diff = final_date - current_date
    total_seconds = int(time_diff.total_seconds()) + 12800
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days < 0:
        days = hours = minutes = seconds = 0

    return [days, hours, minutes, seconds]

def hex_to_rgba(hex_color, alpha=255):
    """
    Converte uma cor hexadecimal para RGBA.
    :param hex_color: Cor no formato hexadecimal (#RRGGBB ou #RGB)
    :param alpha: Transparência (0-255)
    :return: Tupla (R, G, B, A)
    """
    hex_color = hex_color.lstrip('#')

    if len(hex_color) == 3:  # Formato curto #RGB
        hex_color = ''.join([c * 2 for c in hex_color])

    if len(hex_color) != 6:
        raise ValueError("A cor hexadecimal deve ter 6 caracteres (#RRGGBB) ou 3 caracteres (#RGB).")

    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return (r, g, b, alpha)

def get_background_image(background_image_url):
    """
    Busca uma imagem.
    :param background_image_url: ULR da Imagem
    :return: Imagem redimencionada (600 x 150)
    """
    if background_image_url:
        response = requests.get(background_image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            return image.resize((600, 150))
    return None

def get_font_path(font_url):
    """
    Faz o download da fonte a partir de uma URL e salva-a temporariamente.
    :param font_url: URL da fonte
    :return: Caminho para o arquivo da fonte baixada
    """
    if font_url:
        if font_url != '':
            return font_url
        
    return './fonts/NexaRustScriptLDemo-1.otf'

def create_frame(time_remaining, font, background_image=None, background_color='#fff'):
    """
    Configuração e posicionamento a imagem e texto.
    :param hex_color: Cor no formato hexadecimal (#RRGGBB ou #RGB)
    :param alpha: Transparência (0-255)
    :return: Tupla (R, G, B, A)
    """
    font_color_rgba = hex_to_rgba(font_color)
    if background_image:
        background = background_image.copy()
    else:
        background = Image.new("RGBA", (600, 150), hex_to_rgba(background_color))
    
    draw = ImageDraw.Draw(background)


    
    for i in range(len(time_remaining)):
        if time_remaining[i] < 10:
            number_text = f'0{str(time_remaining[i])}'
        else:
            number_text = str(time_remaining[i])

        # Get image size
        text_box = draw.textbbox((0, 0), number_text, font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]

        # Get box size
        box_width = boxSizes[i]["boxEnd"]["x"] - boxSizes[i]["boxStart"]["x"]
        box_height = boxSizes[i]["boxEnd"]["y"] - boxSizes[i]["boxStart"]["y"]

        # Get Offsets
        box_offset_x = (box_width - text_width) // 2
        box_offset_y = (box_height - text_height) // 2
        global_offset_x = boxSizes[i]["boxStart"]["x"] + box_offset_x
        global_offset_y = boxSizes[i]["boxStart"]["y"] + box_offset_y - fontMarginOffset


        text_position = (global_offset_x, global_offset_y)
        draw.text(text_position, number_text, font=font, fill=font_color_rgba)

    return background




# Configuração inicial
final_date_obj = datetime.strptime(final_date, '%Y-%m-%d %H:%M')
current_date_obj = datetime.now()

font_path = get_font_path(font_family)
font = ImageFont.truetype(font_path, font_size)
background_image = get_background_image(background_image_url)

frames = []


# TODO Criar HTML para fazer um preview e mostrar o link no qual ficará hospedado o GIF
# TODO Revisar o FOR
# Geração dos frames
no_loop = False

for seconds_left in range(seconds_to_count, -1, -1):
    time_remaining = calculate_time_remaining(
        final_date_obj - timedelta(seconds=(seconds_to_count - seconds_left)),
        current_date_obj
    )
    
    frame = create_frame(time_remaining, font, background_image, background_color)
    frames.append(frame)
    
    if time_remaining == all(i == time_remaining[0] for i in time_remaining):
        # Gera apenas 1 frame se chegar a "0 00:00:00"
        no_loop = True
        break

# # Salvar GIF
os.makedirs('./imgs', exist_ok=True)
gif_path = './imgs/countdown.gif'


if len(frames) == 1:
    # Apenas um frame se for "0 00:00:00"
    frames[0].save(gif_path, format="PNG")
else:
    # Cria o GIF com repetição
    if no_loop:
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=1000
        )
    else:
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=1000,
            loop=0
        )
