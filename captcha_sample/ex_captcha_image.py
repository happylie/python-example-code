# -*- coding: utf-8 -*-
import io
import base64
from captcha.image import ImageCaptcha

image = ImageCaptcha()

captcha_text = '1234'

image.write(captcha_text, 'sample/1234.png')

data = image.generate(captcha_text)
image_data_b64 = "data:image/png;base64," + base64.b64encode(io.BytesIO(data.read()).getvalue()).decode(
            "utf-8")

print(image_data_b64)
