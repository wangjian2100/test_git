from tkinter import ttk, font

import tkinter as tk

from commom.gui.Gui_Set import MainGuiSet, browse_directory, browse_file


class GUI1:
    def __init__(self, root):
        self.root = root
        # self.set_window()
        self.default_font = None
        # 创建输入表
        self.lst_tab = None
        # 创建子页面列表
        self.dict_tab_obj = {}
        self.son_tab = []
        self.lst_dict_frame = []
        self.frame_row_start = 0
        self.lst_browse_entry = []
        self.initial_dir = None
        # 显示文本控件
        self.display_text = None


class GuiDao1:
    def __init__(self, root, gui_run):
        self.gui = GUI(root)
        self.gui_config = None
        self.gui_run = gui_run

    def set_value(self):
        self.gui_config = self.gui_run.gui_config
        self.gui.root.title(self.gui_config.program_name)  # '高层建筑侧向刚度平衡抗震设计 爱奥尼（Ionic1.0）')
        self.gui.root.geometry(self.gui_config.geometry)  # '1000x1000')
        self.gui.lst_tab = self.gui_run.in_ctrl.lst_tab_ctrl
        # 创建一个字体对象
        self.gui.default_font = font.Font(family='Segoe UI', size=12)
        # 设置所有控件的默认字体
        self.gui.root.option_add('*Font', self.gui.default_font)

    def create_multi_tab(self):
        # 创建一个样式对象
        style = ttk.Style(self.gui.root)
        # 设置子页面名称的字体样式
        style.configure('TNotebook.Tab', font=self.gui.default_font)
        # 创建主页面
        tab_control = ttk.Notebook(self.gui.root)
        MainGuiSet.main_tab = tab_control
        self.create_main_tab(tab_control)
        self.create_2nd_tab(tab_control)
        # 创建多个子页面
        # tab_control = self.tab_control
        for tab in self.gui.lst_tab:
            tab_name = tab.name
            lst_frame_ctrl = tab.lst_frame_ctrl
            self.create_tab(tab_control, tab_name, lst_frame_ctrl)
        # 创建其他子页面
        self.create_other_tab(tab_control)

    def create_tab(self, tab_control, tab_name, lst_frame_ctrl):
        # 创建子页面
        tab_object = ttk.Frame(tab_control)
        # 按钮控件放置的空间
        MainGuiSet.Lst_Ctrl_Tab.append(tab_object)
        self.gui.son_tab.append(tab_object)

        for frame_ctrl in lst_frame_ctrl:
            dict_frame, frame_for_test_gui = self.create_frame(tab_object, frame_ctrl)
            self.gui.lst_dict_frame.append(dict_frame)

        # 创建Frame控件
        tab_control.add(tab_object, text=tab_name)
        tab_control.grid(row=1, column=0, padx=10, pady=10)

    def create_frame(self, parent, frame_ctrl):
        dict_ctrl_group = frame_ctrl.dict_ctrl_group
        v0 = dict_ctrl_group[0]
        frame_text = v0.name
        len1 = len(dict_ctrl_group)
        dict_frame = {}
        # 创建Frame控件
        frame = tk.Frame(parent, width=800, height=100 * len1, bd=1, relief=tk.GROOVE, borderwidth=1)
        frame.grid(row=self.gui.frame_row_start, column=0, sticky='w')
        self.gui.frame_row_start = self.gui.frame_row_start + len1
        # 在Frame中添加名称标签
        label_name = tk.Label(frame, text=frame_text)
        label_name.grid(row=0, column=0, sticky='w', pady=(10, 0))  # 使用pady参数设置垂直间距
        return GuiDao.create_multi_ctrl(frame, frame_text, frame_ctrl, dict_frame, dict_ctrl_group)

    @classmethod
    def create_multi_ctrl(cls, frame, frame_text, frame_ctrl, dict_frame, dict_ctrl_group):
        dict_frame[frame_text] = frame
        # 读取checkbutton值
        for i, ctrl_group in dict_ctrl_group.items():
            if i != 0:
                label_text = ctrl_group.name
                ctrl = ctrl_group.ctrl_name
                if ctrl == 'Label':
                    label_name = tk.Label(frame, text=label_text)
                    label_name.grid(row=1 + i, column=0, sticky='w', pady=(10, 0))  # 使用pady参数设置垂直间距

                if ctrl == 'filedialog':
                    label1 = tk.Label(frame, text=label_text)
                    label1.grid(row=1 + i, column=0, sticky='w', pady=(10, 0))
                    browse_entry = tk.Entry(frame, width=40)
                    browse_entry.grid(row=1 + i, column=1, padx=10)
                    initial_dir = ctrl_group.value
                    browse_button = tk.Button(frame, text='Browse',
                                              command=browse_directory(browse_entry, initial_dir))
                    browse_button.grid(row=1 + i, column=2)  # 改变Browse按钮的位置到第0行，第1列
                    value = ctrl_group.value
                    browse_entry.insert(0, value)
                    dict_frame[label_text] = browse_entry
                    ctrl_group.ctrl_object = browse_entry
                if ctrl == 'filedialog_file':
                    label1 = tk.Label(frame, text=label_text)
                    label1.grid(row=1 + i, column=0, sticky='w', pady=(10, 0))
                    browse_entry = tk.Entry(frame, width=50)
                    browse_entry.grid(row=1 + i, column=1, padx=10)
                    initial_dir = ctrl_group.value
                    browse_button = tk.Button(frame, text='Browse',
                                              command=browse_file(browse_entry, initial_dir))
                    browse_button.grid(row=1 + i, column=2)  # 改变Browse按钮的位置到第0行，第1列
                    value = ctrl_group.value
                    browse_entry.insert(0, value)
                    dict_frame[label_text] = browse_entry
                    ctrl_group.ctrl_object = browse_entry
                if ctrl == 'Entry':
                    value = ctrl_group.value
                    # , width = len(value) + 2
                    if isinstance(value, str):
                        str_value = value
                    else:
                        str_value = str(value)

                    # 创建一个StringVar对象
                    entry_text = tk.StringVar()

                    label1 = tk.Label(frame, text=label_text)
                    label1.grid(row=1 + i, column=0, sticky='w', pady=(10, 0))
                    entry1 = tk.Entry(frame, width=len(str_value) + 12, textvariable=entry_text)
                    entry1.grid(row=1 + i, column=1, sticky='w', padx=10)

                    entry1.insert(0, value)
                    dict_frame[label_text] = entry1
                    ctrl_group.ctrl_object = entry1

                    attribute = ctrl_group.attribute

                    MainGuiSet.dict_entry_text[attribute] = entry_text
                # *************************************************************************

                elif ctrl == 'Combobox':
                    value = ctrl_group.value
                    if isinstance(value, int):
                        anchor1 = 'right'

                    else:
                        if value.isdigit():
                            anchor1 = 'right'
                        else:
                            anchor1 = 'w'

                    label1 = tk.Label(frame, text=label_text)
                    label1.grid(row=1 + i, column=0, sticky='w', pady=(10, 0))
                    values = ctrl_group.note2.split(',')
                    cb = ttk.Combobox(frame, values=values, width=len(str(value)) + 2, justify=anchor1)

                    cb.set(value)
                    cb.grid(row=1 + i, column=1, sticky='w', padx=10)
                    dict_frame[label_text] = cb
                    ctrl_group.ctrl_object = cb
                    attribute = ctrl_group.attribute
                    MainGuiSet.dict_combobox_text[attribute] = cb

        return dict_frame, frame

    def create_main_tab(self, tab_control):
        tab_object = ttk.Frame(tab_control)
        # 保存页面到公共变量
        MainGuiSet.Lst_Ctrl_Tab.append(tab_object)
        # 按钮控件放置的空间
        tab_control.add(tab_object, text='主页')
        print('**创建', '主页', '子页面')
        program_english_name = self.gui_config.program_english_name
        font_high_english_name = self.gui_config.font_high_english_name
        program_chinese_name = self.gui_config.program_chinese_name
        font_high_chinese_name = self.gui_config.font_high_chinese_name
        tab_control.grid(row=1, column=0, padx=10, pady=10)
        label_name = tk.Label(tab_object, text=program_english_name, font=('Arial', font_high_english_name))
        label_name.grid(row=2, column=3, sticky='s', pady=(10, 0))
        label_name = tk.Label(tab_object, text=program_chinese_name, font=('KaiTi', font_high_chinese_name))
        label_name.grid(row=3, column=3, sticky='s', pady=(10, 0))

    def create_2nd_tab(self, tab_control):
        pass

    def create_other_tab(self, tab_control):
        pass

    def run_file_do(self):
        print('**执行 run_file_do 命令')
