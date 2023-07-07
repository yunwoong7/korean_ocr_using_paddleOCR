import cv2
from paddleocr import PaddleOCR, draw_ocr
from utils.image_util import plt_imshow, put_text
from paddleocr.paddleocr import MODEL_URLS


class MyPaddleOCR:
    def __init__(self, lang: str = "korean", **kwargs):
        self.lang = lang
        self._ocr = PaddleOCR(lang="korean")
        self.img_path = None
        self.ocr_result = {}
    
    def get_available_langs(self):
        langs_info = []

        for idx, model_name in enumerate(list(MODEL_URLS['OCR'].keys())):
            for lang in list(MODEL_URLS['OCR'][model_name]['rec'].keys()):
                if lang not in langs_info:
                    langs_info.append(lang)
        
        print('Available Language : {}'.format(langs_info))
        
    def get_available_models(self):
        model_info = {}

        for idx, model_name in enumerate(list(MODEL_URLS['OCR'].keys())):
            model_info[model_name] = list(MODEL_URLS['OCR'][model_name]['rec'].keys())
            print('#{} Model Vesion : [{}] - Language : {}'.format(idx+1, model_name, list(MODEL_URLS['OCR'][model_name]['rec'].keys())))
        
    def get_ocr_result(self):
        return self.ocr_result

    def get_img_path(self):
        return self.img_path

    def show_img(self):
        plt_imshow(img=self.img_path)
        
    def run_ocr(self, img_path: str, debug: bool = False):
        self.img_path = img_path
        ocr_text = []
        result = self._ocr.ocr(img_path, cls=False)
        self.ocr_result = result[0]

        if self.ocr_result:
            for r in result[0]:
                ocr_text.append(r[1][0])
        else:
            ocr_text = "No text detected."

        if debug:
            self.show_img_with_ocr()

        return ocr_text
    
    def show_img_with_ocr(self):
        img = cv2.imread(self.img_path)
        roi_img = img.copy()

        for text_result in self.ocr_result:
            text = text_result[1][0]
            tlX = int(text_result[0][0][0])
            tlY = int(text_result[0][0][1])
            trX = int(text_result[0][1][0])
            trY = int(text_result[0][1][1])
            brX = int(text_result[0][2][0])
            brY = int(text_result[0][2][1])
            blX = int(text_result[0][3][0])
            blY = int(text_result[0][3][1])

            pts = ((tlX, tlY), (trX, trY), (brX, brY), (blX, blY))

            topLeft = pts[0]
            topRight = pts[1]
            bottomRight = pts[2]
            bottomLeft = pts[3]

            cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 2)
            roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 20, font_size=15)

            # print(text)

        plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))
