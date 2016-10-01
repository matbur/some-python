from tools import is_image, get_img_path


class Answer(object):
    def __init__(self, text, base, is_true=False):
        self.text = text
        self.is_true = is_true
        self.is_img = is_image(text, base)
        self.img_path = get_img_path(self.is_img, self.text, base)

    def __repr__(self):
        return '{is_true}:{is_img} {text}'.format(**self.__dict__)
