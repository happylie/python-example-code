# -*- coding: utf-8 -*-
import io
import base64
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

captcha_text = '1234'

audio.write(captcha_text, 'sample/1234.wav')