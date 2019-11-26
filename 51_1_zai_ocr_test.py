import zAI
from zAI import zImage

zAI.utils.set_backend_key(key_name='MICROSOFT_AZURE_VISION_API_KEY',key_value='197245a8c7f14fe1bd6ee9ca025c3643',save=True)
#AZURE에서 얻은 API KEY id: teakhyun@0365dge.net
zAI.utils.set_backend_key(key_name='MICROSOFT_AZURE_URL', key_value='koreacentral.api.cognitive.microsoft.com',save=True)
#책 70페이지 key_value부분 틀림. 한국중부로 셋팅

image= zImage('./img/test.png')
image.display()

text = image.ocr(backend='Microsoft')
text.display()
