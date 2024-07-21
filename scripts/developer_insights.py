from modules import scripts
from modules.processing import StableDiffusionProcessing

from lib.developer_insights.logger import logger
from src.developer_insights.extension import extensionTitle

templateBracketLeft = '{{'
templateBracketRight = '}}'

normalFontSize = 32 # for 1024x1024 pixels or anything with the same megapixel value
hookType = 'postprocess_image'

keysFromImg = [
  'cfg_scale',
  'width',
  'height',
  'seed',
  'subseed',
  'prompt',
  'negative_prompt',
]

specialReplacements = {
  'all_seeds': 'seed',
  'all_subseeds': 'subseed',
  'all_prompts': 'prompt',
  'all_negative_prompts': 'negative_prompt',
}

class CustomTextOverlay(scripts.Script):
  def title(self):
    return extensionTitle

  def show(self, is_img2img):
    return scripts.AlwaysVisible

  def process(
    self, processing: StableDiffusionProcessing, enabled: bool, textScale: int, textColor: str, backgroundColor: str, backgroundOpacity: int, paddingScale: int, marginScale: int, outlineScale: int, outlineColor: str, outlineOpacity: int, textEnabled1: bool, textEnabled2: bool, textEnabled3: bool,
    textEnabled4: bool, textEnabled5: bool, textEnabled6: bool, textEnabled7: bool, textEnabled8: bool, textEnabled9: bool, textTemplate1: str, textTemplate2: str, textTemplate3: str, textTemplate4: str, textTemplate5: str, textTemplate6: str, textTemplate7: str, textTemplate8: str,
    textTemplate9: str
  ):
    logger.info('process')

  def postprocess_image(self, processing: StableDiffusionProcessing, processed):
    logger.info('postprocess_image')
