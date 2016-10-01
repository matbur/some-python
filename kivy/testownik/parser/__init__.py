import sys
from glob import glob

from answer import Answer
from base import Base
from question import Question
from tools import read_file, join_path


# TODO: encoding files

def parse(base_dir):
    _base = Base()

    for filename in sorted(glob(join_path(base_dir, '*.txt'))):
        read, err = read_file(filename)

        if err:
            sys.exit(err)

        keys = read[0][1:]
        question_text = read[1]
        answers_text = read[2:]

        answers = [Answer(ans, base_dir) for ans in answers_text]
        for i, v in enumerate(keys):
            answers[i].is_true = (v == '1')

        _question = Question(filename, question_text, answers, base_dir)
        _base.questions.append(_question)

    return _base
