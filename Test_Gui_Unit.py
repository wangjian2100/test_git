import os

from commom.gui.In_Ctrl_Dao import FrameCtrlDao

class TestGuiUnit:
    def __init__(self):
        #输入
        self.word_one = None
        self.test_one = None
        self.score_one = None
        #题目
        self.exam_num = None  # 题号
        self.lst_question = None
        self.lst_question_text = None
        self.lst_select = []  # 用户选择****************
        #容器
        # self.container=None

class TestGuiUnitDao:
    def __init__(self):
        self.test_gui_unit = None
        self.test_set = None

    def set_value(self, exam_num, test_set, word_one, test_one):
        self.test_set = test_set
        self.test_gui_unit = TestGuiUnit()
        self.test_gui_unit.exam_num = exam_num  # 题号
        self.test_gui_unit.word_one = word_one
        self.test_gui_unit.test_one = test_one

    def convert_frame_ctrl(self):
        answer_select = self.test_set.answer_select

class TestScore:
    def __init__(self):
        self.dict_score = None  # { 1:}
        self.time = None
        self.score = None
        self.lst_wrong_index = None
        self.dict_origin_word = None
        self.dict_wrong_word = None
