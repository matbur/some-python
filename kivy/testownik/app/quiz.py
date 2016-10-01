from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

from parser import parse


class QuestionLabel(Label):
    def __init__(self, **kwargs):
        super(QuestionLabel, self).__init__(**kwargs)
        self._question = None

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, que):
        self.restore_default()

        self._question = que
        if que.is_img:
            img = Image(source=que.img_path)
            img.pos = self.pos
            img.size = self.size
            self.add_widget(img)
        else:
            self.text = que.text

    def restore_default(self):
        self.clear_widgets()
        self.text = ''


class AnswerButton(ToggleButton):
    def __init__(self, answer, **kwargs):
        super(AnswerButton, self).__init__(**kwargs)
        self.answer = answer

    def update_text(self, i):
        self.y = self.height * i

        ans = self.answer
        if ans.is_img:
            img = Image(source=ans.img_path)
            img.pos = self.pos
            img.size = self.size
            self.add_widget(img)
        else:
            self.text = ans.text


class Quiz(Screen):
    check_button = ObjectProperty()
    next_button = ObjectProperty()
    question_label = ObjectProperty()
    answers_panel = ObjectProperty()

    def __init__(self, **kwargs):
        super(Quiz, self).__init__(**kwargs)

        self.base = None
        self.actual_question = None
        self.previous_question = None

    def set_base(self, base):
        self.base = parse(base)
        self.base.shuffle_questions()
        self.get_next()

    def check_answer(self):
        true_answers = filter(lambda x: x.is_true, self.actual_question.answers)
        answers = self.answers_panel.children
        for ans_button in answers:
            if ans_button.answer in true_answers:
                ans_button.background_color = [0, 1, 0, 1]

            elif ans_button.state == 'down':
                ans_button.background_color = [1, 0, 0, 1]

    def get_next(self):
        self.random_new_question()
        self.update_question_label()
        self.create_answers()

    def random_new_question(self):
        self.previous_question = self.actual_question
        self.actual_question = self.base.get_random_question()
        self.actual_question.shuffle_answers()

    def update_question_label(self):
        self.question_label.question = self.actual_question

    def create_answers(self):
        parent = self.answers_panel
        parent.clear_widgets()
        answers = self.actual_question.answers
        height = parent.height / len(answers)
        for i, answer in enumerate(answers):
            ans = AnswerButton(answer, size=(parent.width, height))
            ans.update_text(len(answers) - i - 1)
            self.answers_panel.add_widget(ans)
