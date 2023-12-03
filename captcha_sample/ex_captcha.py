# -*- coding: utf-8 -*-
import random
import io
import base64
import string
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha


def _random_code(length=8, captcha_type=None):
    """
    Random Code Generate
    :param length: Default Length 8
    :captcha_type: None, audio
    :return:
    """
    custom_punctuation = '#%&?$'
    custom_lowercase = 'abdefghjqrt'
    custom_uppercase = 'ABDEFGHJLQRT'
    custom_digits = '2345678'
    if captcha_type == 'audio':
        return "".join(random.choice(string.digits) for _ in range(length))
    allowed_code = custom_digits + custom_uppercase + custom_lowercase + custom_punctuation
    return "".join(random.choice(allowed_code) for _ in range(length))


class MakeCaptchaAudio:
    def __init__(self):
        self.audio = AudioCaptcha()
        self.captcha_text = _random_code(captcha_type="audio")
        self.ret = ""

    def set_save_audio_file(self) -> bool:
        """
        Set Captcha Audio File Save(File Type : WAV)
        :return:
        """
        try:
            self.audio.write(self.captcha_text, f'sample/output.wav')
            return True
        except Exception as err:
            return False


class MakeCaptchaImg:
    def __init__(self):
        self.width: int = 250
        self.height: int = 100
        self.font_sizes: tuple = (50, 58, 64)
        self.image = ImageCaptcha(self.width, self.height, font_sizes=self.font_sizes)
        self.audio = AudioCaptcha()
        self.captcha_text = _random_code()
        self.ret = ""

    def captcha_valid(self, text) -> bool:
        """
        Captcha Valid
        :param text:
        :return:
        """
        if self.captcha_text != text:
            return False
        return True

    def get_base64_image_data(self):
        """
        Get Captcha Base64 Image Data(File Type : PNG)
        :return:
        """
        image_data = self.image.generate(self.captcha_text)
        image_data_b64 = "data:image/png;base64," + base64.b64encode(io.BytesIO(image_data.read()).getvalue()).decode(
            "utf-8")
        return image_data_b64

    def set_save_image_file(self) -> bool:
        """
        Set Captcha Image File Save(File Type : PNG)
        :return:
        """
        try:
            self.image.write(self.captcha_text, f'sample/output.png')
            return True
        except Exception as err:
            return False


if __name__ == "__main__":
    # CAPTCHA Audio
    captcha_audio = MakeCaptchaAudio()
    print(f'CAPTCHA Text: {captcha_audio.captcha_text}')
    print(f'Save Audio: {captcha_audio.set_save_audio_file()}')

    # CAPTCHA Image
    captcha_img = MakeCaptchaImg()
    print(f'CAPTCHA Text: {captcha_img.captcha_text}')
    print(f'Base64 Image: {captcha_img.get_base64_image_data()}')
    print(f'Save Image: {captcha_img.set_save_image_file()}')
    print(f'CAPTCHA Valid: {captcha_img.captcha_valid(captcha_img.captcha_text)}')
    print(f'CAPTCHA Valid: {captcha_img.captcha_valid("1234")}')
