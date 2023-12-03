# -*- coding: utf-8 -*-
import random
import io
import base64
from captcha.image import ImageCaptcha


class MakeCaptcha:
    def __init__(self):
        self.width: int = 250
        self.height: int = 100
        self.font_sizes: tuple = (50, 58, 64)
        self.image = ImageCaptcha(self.width, self.height, font_sizes=self.font_sizes)
        self.captcha_text = self.__random_code()
        self.ret = ""

    @staticmethod
    def __random_code(length=8):
        """
        Random Code Generate
        :param length: Default Length 8
        :return:
        """
        custom_punctuation = '#%&?$'
        custom_lowercase = 'abdefghjqrt'
        custom_uppercase = 'ABDEFGHJLQRT'
        custom_digits = '2345678'
        allowed_code = custom_digits + custom_uppercase + custom_lowercase + custom_punctuation
        return "".join(random.choice(allowed_code) for _ in range(length))

    def captcha_valid(self, text):
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

    def set_save_image_file(self):
        """
        Set Captcha Image File Save(File Type : PNG)
        :return:
        """
        self.image.write(self.captcha_text, f'sample/output.png')


if __name__ == "__main__":
    captcha = MakeCaptcha()
    print(captcha.captcha_text)
    print(captcha.get_base64_image_data())
    captcha.set_save_image_file()
    print(captcha.captcha_valid(captcha.captcha_text))
    print(captcha.captcha_valid('1234'))
