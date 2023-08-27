import copy

from base_dir import YML_FILE_SET
from commom.class_share.Def_Base import print_var
from word_list.Def_word.Yml import load_dict_by_yml
from word_list.word_gui.Ctrl_label import *


class InTab:
    # 表
    def __init__(self):
        # tab文本字典
        self.dict_tab = {}

class InTabDao:
    def __init__(self):
        self.in_tab = InTab()

    def setvar(self,yml_filename=None):
        if yml_filename is None:
            yml_filename = YML_FILE_SET.tab_yml
        in_tab = load_dict_by_yml(yml_filename)
        #dict_tab = copy.deepcopy(in_tab)
        for k_tab, v_tab in in_tab.items():

            for k_frame, v_frame in v_tab.items():

                for k_ctrl, v_ctrl in v_frame.items():

                    class_name='Ctrl'+v_ctrl['ctrl_name']
                    #ctrl_var = globals()[class_name]
                    lst_attr=[]#ctrl_name, name, attribute, data_type, value, note2
                    lst_attr.append(v_ctrl['ctrl_name'])
                    lst_attr.append(v_ctrl['name'])
                    if 'attribute' in v_ctrl:
                        lst_attr.append(v_ctrl['attribute'])
                    if 'data_type' in v_ctrl:
                        lst_attr.append(v_ctrl['data_type'])
                    if 'value' in v_ctrl:
                        lst_attr.append(v_ctrl['value'])
                    if 'note2' in v_ctrl:
                        lst_attr.append(v_ctrl['note2'])
def setvar(obj,lst_ref):
    obj.setvar()

if __name__ == '__main__':
    fn=r'G:\pyt1\heheword\word_list\config\in_tab.yml'
    itd=InTabDao()
    itd.setvar(fn)
    print_var(itd.in_tab.dict_tab)