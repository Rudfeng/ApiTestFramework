import json
import xml.etree.ElementTree as et
import xlrd
import pymysql
import logging
import logging.handlers


def read_json_data(filename):
    """

    :param filname: 路径
    :return:
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        jsonData = json.load(f)  # 数据文件通过json维护
        result = list()
        for login_data in jsonData:
            result.append(tuple(login_data.values()))  # 以list形式返回给parameterized使用
        print(result)
    return result


def read_xml_data(filename):
    """

    :param filename:
    :return:
    """
    tree = et.parse(filename)
    root = tree.getroot()
    param_data_list = []
    for case in root:
        temp_list = []
        for input_data in case.findall("*"):
            temp_list.append(input_data.text)
        param_data_list.append(tuple(temp_list))
    return param_data_list


def read_xls_data(filename):
    """

    :param filename:
    :return:
    """
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    param_data = []
    # sheet.nrows获取表的总行数    sheet.ncols获取表的总列数
    for i in range(1, sheet.nrows):
        # sheet.row_values(i) 获取第i行的数据
        # sheet.col_values(i) 获取第i行的数据
        param_data.append(tuple(sheet.row_values(i)))
    return param_data


def read_sql_data():
    conn = pymysql.connect(host='localhost', port=3306, user="root", password='root', charset='utf-8',
                           database='test_sql')
    cursor = conn.cursor()
    cursor.excute("SELECT * FROM test.test_sql;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def logging_init():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    file_handler = logging.handlers.TimedRotatingFileHandler \
        ("../logs/test_log.log", when='h',
         interval=1, backupCount=3, encoding="utf-8")
    fmt = "%(asctime)s %(levelname)s [%(name)s] " \
          "[ %(filename)s %(funcName)s %(lineno)d ] %(message)s "
    formatter = logging.Formatter(fmt)
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    print(read_xls_data('../data/login_data.xls'))
