import os
import moviepy.editor as mp

__version__ = "0.0.1"


class AudioExtractor(object):
    def __init__(self, path):
        self.path = path
        self.dir = os.path.split(path)[0]
        filename, file_ext = os.path.splitext(path)
        self.filename = filename
        self.file_ext = file_ext[1:]

        self.video_ext = ('mp4', 'avi', 'mkv')
        self.audio_ext = ('mp3', 'wav')

    def get_mp3(self):
        if self.file_ext in self.video_ext:
            self.extract_audio()
        elif self.file_ext in self.audio_ext:
            self.convert_audio()

    def extract_audio(self):
        clip = mp.VideoFileClip(self.path)
        clip.audio.write_audiofile(f"{self.filename}.mp3")

    def convert_audio(self):
        clip = mp.AudioFileClip(self.path)
        clip.write_audiofile(f"{self.filename}.mp3")


if __name__ == "__main__":
    path = input("Введите путь к файлу: ")
    extractor = AudioExtractor(path)
    extractor.get_mp3()