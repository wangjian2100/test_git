class CtrlGroup:
    # 控件组类
    def __init__(self,  ):
        self.name = None
        self.num = None
        self.dict_in_xls = None
        self.ctrl_object = None
        self.sort_num = None
        self.tab_name = None
        self.frame_num = None
        self.ctrl_num = None#
        self.ctrl_name = None#
        self.value = None
        self.attribute = None#
        self.note1 = None
        self.note2 = None
        self.data_type = None#
        self.end_str = None

class FrameCtrl:
    # frame框类
    def __init__(self, ):
        self.name = None
        self.num = None
        self.dict_line_xls = None
        self.dict_ctrl_group = {}
        self.check_vars = []
        # ctrl文本字典
        self.dict_ctrl_text = {}

class TabCtrl:
    # 表
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.lst_frame_ctrl = []
        self.dict_frame_xls = {}
        self.account_write_xls = 0
        # frame文本字典
        self.dict_frame_text = {}



class InCtrl:
    # 全部的表





    def __init__(self, name):
        self.name = name
        self.lst_tab_ctrl = []  # 初始化 页面列表
        self.dict_tab_ctrl = {} # 初始化 页面列表
        #tab文本字典
        self.dict_tab_text = {}
class InDict:
    dict_tab=None
    dict_frame=None
    dict_ctrl=None
    elem_ctrl=None