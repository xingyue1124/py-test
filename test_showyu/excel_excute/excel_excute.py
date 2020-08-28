from test_showyu.data_driver.excel_config import ExcelCof
from test_showyu.framework.webui_autotest import WebUI_Framework
from test_showyu.log.log import Logger


class ExcelExcute():
    # 创建日志对象
    log = Logger().get_logger()

    # Excel执行读写操作
    def excute_web(self):
        # 实例化对象
        ec = ExcelCof()
        excel_path = '.\excel_excute\WebUICase.xlsx'
        excel = ec.load_excel(excel_path)
        sheets = ec.get_sheets(excel)
        try:
            # 读取所有sheet页
            for sheet in sheets:
                self.log.info('获取{0}内容成功，现在开始执行自动化测试......'.format(sheet))
                sheet1 = excel[sheet]
                # 基于sheet内容，运行测试用例
                for value in sheet1.values:
                    param = {}
                    param['loc'] = value[2]
                    param['value'] = value[3]
                    param['txt'] = value[4]
                    param['expect'] = value[6]
                    # 判断文件，从用例内容开始执行
                    if type(value[0]) is int:
                        # 判断关键字列，如果是open_browser，则实例化对象，如果不是，则进行其他元素操作
                        if value[1] == 'open_browser':
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            wf = WebUI_Framework(param['txt'])
                        # 判断是否为断言，若是断言则添加写入操作
                        elif 'assert' in value[1]:
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            status = getattr(wf, value[1])(**param)
                            row = value[0] + 1
                            if status is True:
                                self.log.info('流程测试通过！')
                                ec.cell_write('pass', sheet1, row)
                            else:
                                self.log.info('流程测试失败！')
                                ec.cell_write('false', sheet1, row)
                            # 保存数据
                            ec.save_excel(excel, excel_path)
                        # 定义常规关键字调用
                        else:
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            getattr(wf, value[1])(**param)
                    else:
                        pass
        except Exception as e:
            self.log.exception('运行出现异常，信息描述：{0}'.format(e))
        finally:
            # 关闭读取的文件
            self.log.info("文件读取完毕，自动化执行结束！\n")
            ec.close(excel)
