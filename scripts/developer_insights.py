from modules import scripts
from modules.processing import StableDiffusionProcessing

from lib.developer_insights.logger import logger
from src.developer_insights.extension import extensionTitle

class CustomTextOverlay(scripts.Script):
  def title(self):
    return extensionTitle

  def show(self, is_img2img):
    return scripts.AlwaysVisible

  def process(self, processing: StableDiffusionProcessing):
    logger.info('process')

  def postprocess_image(self, processing: StableDiffusionProcessing, processed):
    logger.info('postprocess_image')
