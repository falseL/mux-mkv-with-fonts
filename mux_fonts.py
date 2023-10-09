from pymkv import MKVAttachment
from pymkv import MKVFile
import os
from concurrent.futures import ThreadPoolExecutor

fonts_folder = 'fonts/'
videos_folder = 'videos/'
output_folder = 'output/'

def get_file_list(folder, ext = None):
    file_list = []
    for file in os.listdir(folder):
        if ext is None:
            file_list.append(file)
        elif file.endswith(ext):
            file_list.append(file)
    return file_list

def add_font_to_mkv(mkv, font):
    attachment = MKVAttachment(fonts_folder + font, name=font)
    attachment.mimetype = 'application/x-truetype-font'
    attachment.description = font
    mkv.add_attachment(attachment)

def mux_video_with_fonts(video, fonts):
    mkv = MKVFile(videos_folder + video)
    for font in fonts:
        add_font_to_mkv(mkv, font)
    mkv.mux(output_folder + video)
    print('Muxed ' + video)

def mux_all_videos_with_fonts():
    videos = get_file_list(videos_folder, '.mkv')
    fonts = get_file_list(fonts_folder)
    executor = ThreadPoolExecutor()
    for video in videos:
        executor.submit(mux_video_with_fonts, video, fonts)

if __name__ == "__main__":
    mux_all_videos_with_fonts()