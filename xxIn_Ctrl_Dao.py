import copy

import pandas as pd

from base_dir import YML_FILE_SET
from commom.class_share.Def_Base import   get_dict_attr
from commom.gui.xxIn_Ctrl import CtrlGroup, InDict, TabCtrl, InCtrl, FrameCtrl
from word_list.Def_word.Yml import load_var_by_yml, save_yml


class CtrlGroupDao:
    def __init__(self, ):
        self.ctrl_group = CtrlGroup()

    def setvar_by_xls(self, name, num, dict_line_xls):
        self.ctrl_group.name = name
        self.ctrl_group.num = num
        self.ctrl_group.dict_in_xls = dict_line_xls

    def set_value_by_xls(self):
        """{'名称': '基本输入', '备注': nan, '子页面': 'base', '属性': nan,
                    '序号': 1, '控件名': 'Label', '控件序号': 0,
                    '框架': 1, '缺省值': '-------------------', '说明': 'frame'}"""
        d = self.ctrl_group.dict_in_xls
        self.ctrl_group.sort_num = d['序号']
        self.ctrl_group.tab_name = d['子页面']
        self.ctrl_group.frame_num = d['框架']
        self.ctrl_group.ctrl_num = d['控件序号']

        self.ctrl_group.ctrl_name = d['控件名']
        self.ctrl_group.value = d['缺省值']

        self.ctrl_group.attribute = d['属性']
        self.ctrl_group.note1 = d['说明']
        self.ctrl_group.note2 = d['备注']
        self.ctrl_group.data_type = d['数据类型']

    @load_var_by_yml
    def globals_var(self, class_name):
        class_var = globals()[class_name]
        return class_var

    def get_var_by_yml(self, fn):
        index = self.globals_var('CtrlGroup', fn)
        return index


class FrameCtrlDao:
    def __init__(self):
        self.frame_ctrl = FrameCtrl()

    def setvar_by_xls(self, name, num, dict_line_xls):
        self.frame_ctrl.name = name
        self.frame_ctrl.num = num
        self.frame_ctrl.dict_line_xls = dict_line_xls

    def set_value(self):
        d = self.frame_ctrl.dict_line_xls
        k=1
        for i, v in d.items():
            name = v['名称']
            num = v['控件序号']
            ctrl_group_dao = CtrlGroupDao()
            ctrl_group_dao.setvar_by_xls(name, num, v)

            ctrl_group_dao.set_value_by_xls()
            ctrl_group = ctrl_group_dao.ctrl_group

            self.frame_ctrl.dict_ctrl_group[num] = ctrl_group
            ctrl_group1 = copy.copy(ctrl_group)
            if ctrl_group1.ctrl_name=='Label':
                del ctrl_group1.data_type
                del ctrl_group1.note2
                del ctrl_group1.attribute
                del ctrl_group1.value
            if ctrl_group1.ctrl_name=='Entry':
                #del ctrl_group1.num
                del ctrl_group1.note2
            if ctrl_group1.ctrl_name == 'filedialog':
                # del ctrl_group1.num
                del ctrl_group1.note2
            del ctrl_group1.end_str
            del ctrl_group1.num
            del ctrl_group1.dict_in_xls
            del ctrl_group1.ctrl_object
            del ctrl_group1.frame_num
            del ctrl_group1.tab_name
            del ctrl_group1.sort_num
            del ctrl_group1.note1
            del ctrl_group1.ctrl_num
            elem_ctrl = get_dict_attr(ctrl_group1)  # InDict.dict
            InDict.dict_ctrl['ctrl' + str(i + 1)] = elem_ctrl  # InDict.dict
            #   构造控件文本字典
            self.frame_ctrl.dict_ctrl_text['ctrl_'+str(k)]=get_dict_attr(ctrl_group1)
            k+=1


def read_xls(excel_file, sheet_name):
    # 读取 Excel 表格中的特定工作表的全部单元格
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # 一个以索引作为外层字典键的内层字典，内层字典key列名，value为单元格数值。

    data = df.to_dict(orient='index')

    return data


class TabCtrlDao:
    def __init__(self, name, num):
        self.tab_ctrl = TabCtrl(name, num)

    def set_lst_frame_ctrl_by_xls(self, excel_file, sheet_name):
        # 制作FrameCtrl的列表
        self.set_dict_xls_frame(excel_file, sheet_name)
        dict_frame_xls = self.tab_ctrl.dict_frame_xls
        i = 0
        InDict.dict_ctrl = {}  # InDict.dict
        for k, v in dict_frame_xls.items():
            min_index = min(v.keys())
            name = v[min_index]['名称']
            num = i

            frame_ctrl_dao = FrameCtrlDao()
            frame_ctrl_dao.setvar_by_xls(name, num, v)

            frame_ctrl_dao.set_value()
            frame_ctrl = frame_ctrl_dao.frame_ctrl
            self.tab_ctrl.lst_frame_ctrl.append(frame_ctrl)
            i += 1

            dict_ctrl = copy.deepcopy(InDict.dict_ctrl)
            InDict.dict_frame['frame' + str(i)] = dict_ctrl  # InDict.dict
            #   构造frame文本字典
            self.tab_ctrl.dict_frame_text['frame_'+str(k+1)]=frame_ctrl.dict_ctrl_text
    def set_dict_xls_frame(self, excel_file, sheet_name):
        # 獲取控制表格中的每個frame的字典
        dict_all = read_xls(excel_file, sheet_name)
        j = 0
        dict_xls_frame = {}
        start_num = 0
        for i, v in dict_all.items():
            v3 = v['控件序号']
            if i != 0 and v3 == 0:
                end_num = i - 1
                dict_xls_frame[j] = {key: dict_all[key]
                                     for key in dict_all.keys() if start_num <= key <= end_num}
                j = j + 1
                start_num = i
        dict_xls_frame[j + 1] = {key: dict_all[key]
                                 for key in dict_all.keys()
                                 if start_num <= key <= i}
        self.tab_ctrl.dict_frame_xls = dict_xls_frame


class InCtrlDao:
    def __init__(self, name, in_setting_xls_filename, lst_sheet_name):
        self.in_ctrl = InCtrl(name)
        self.lst_sheet_name = lst_sheet_name
        self.xls_filename = in_setting_xls_filename

    def set_value(self):
        # 输入数据
        dict_in_ctrl = {}
        lst_tab_ctrl = []
        xls_filename = self.xls_filename
        lst_sheet_name = self.lst_sheet_name
        i = 0
        InDict.dict_tab = {}  # InDict.dict
        for sheet_name in lst_sheet_name:
            tab_ctrl_dao = TabCtrlDao(sheet_name, i)
            tab_ctrl = tab_ctrl_dao.tab_ctrl
            InDict.dict_frame = {}  # InDict.dict
            tab_ctrl_dao.set_lst_frame_ctrl_by_xls(xls_filename, sheet_name)
            lst_tab_ctrl.append(tab_ctrl)

            i += 1
            # InDict.dict
            dict_frame = copy.deepcopy(InDict.dict_frame)
            InDict.dict_tab[sheet_name + str(i - 1)] = dict_frame  # InDict.dict
            #   构造tab文本字典
            self.in_ctrl.dict_tab_text['tab_'+sheet_name] = tab_ctrl.dict_frame_text

        self.in_ctrl.lst_tab_ctrl = lst_tab_ctrl



    def save_ctrl(self):
        #输出控件字典
        dict_tab_text=self.in_ctrl.dict_tab_text
        yml='G:\wordlist\sys\dict_tab_text.yml'
        yml= YML_FILE_SET.dict_tab_text_file
        save_yml(yml,dict_tab_text)
