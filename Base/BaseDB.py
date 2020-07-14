import pymysql

import logging

from Base.BaseSettings import *


class MonitorDB:
    logger = logging.getLogger(__name__)

    def __init__(self, **db_config):
        if not db_config:
            db_config = dict(
                host=MYSQL_HOST,
                db=MYSQL_DBNAME,
                user=MYSQL_USER,
                passwd=MYSQL_PASSWD,
                port=MYSQL_PORT,
                charset='utf8',
            )
        try:
            conn = pymysql.connect(**db_config)
            conn.autocommit(True)
            # self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            self.conn = conn
        except Exception as e:
            self.logger.error('init error:')
            self.logger.error(e)
            raise IOError(e)

    def sql_execute(self, sql, operation=None):
        """
            执行无返回结果集的sql，主要 有insert update delete
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            response = cursor.execute(sql, operation) if operation else cursor.execute(sql)
            # self.logger.debug(response)
        except Exception as e:
            self.logger.debug("MonitorDB   41  ==============================>  执行错误原因:  %s  错误语句　：　%s ", e, sql)
            print(e)
            cursor.close()
            return None
        else:
            cursor.close()
            return response

    def sql_fetch_many(self, sql, operation=None):
        """
            执行有返回结果集的sql,主要是select，返回的是数组
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            response = cursor.execute(sql, operation) if operation else cursor.execute(sql)
        except Exception as e:
            self.logger.error("MonitorDB  54  ==============================>  执行错误原因:  %s  错误语句　：　%s ", e, sql)
            cursor.close()
            return None, None
        else:
            data = cursor.fetchall()
            cursor.close()
            return response, data

    def sql_fetch_one(self, sql, operation=None):
        """
            执行有返回结果集的sql,主要是select，范围都是dict
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            response = cursor.execute(sql, operation) if operation else cursor.execute(sql)
        except Exception as e:
            # self.logger.error(sql)
            self.logger.error("MonitorDB  72  ==============================>  执行错误原因:  %s  错误语句　：　%s ", e, sql)
            cursor.close()
            return None, None
        else:
            data = cursor.fetchone()
            cursor.close()
            return response, data

    def sqls_execute(self, sqls, operation=None):
        """
            执行所有sql,返回数据
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            for sql in sqls:
                response = cursor.execute(sql, operation) if operation else cursor.execute(sql)
        except Exception as e:
            self.logger.error(sql)
            self.logger.error(e)
            cursor.close()
            return None, None
        else:
            data = cursor.fetchone()
            cursor.close()
            return response, data

    def sql_execute_many(self, sql, operation=None):
        """
        执行多个sql，主要是insert into 多条数据的时候
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            response = cursor.executemany(sql, operation) if operation else cursor.executemany(sql)
        except Exception as e:
            self.logger.error(sql)
            self.logger.error(e)
            cursor.close()
            return None
        else:
            cursor.close()
            return response

    def sql_execute_with_last_pk(self, sql, operation=None, logger=logger):
        """
        执行sql,返回主键
        """
        try:
            conn = self.conn
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            response = cursor.execute(sql, operation) if operation else cursor.execute(sql)
        except Exception as e:
            logger.error(sql)
            logger.error(e)
            cursor.close()
            return None
        else:
            last_pk = cursor.lastrowid
            cursor.close()
            return last_pk, response

    def close_conn(self):
        try:
            self.conn.close()
        except Exception as e:
            self.logger.error("close error:")
            self.logger.error(e)

    def begin(self):
        """
        @summary: 开启事务
        """
        self.conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self.conn.commit()
        else:
            self.conn.rollback()
        # 设置事务自动提交
        self.commit_auto()

    def commit_auto(self):
        """
        @summary: 事务自动提交
        :return:
        """
        self.conn.autocommit(True)

    def sql_execute_file(self, sqlfilepath):
        with open(sqlfilepath, encoding='utf-8', mode='r') as f:
            # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
            sql_list = f.read().split(';')[:-1]
            for x in sql_list:
                # 判断包含空行的
                if '\n' in x:
                    # 替换空行为1个空格
                    x = x.replace('\n', ' ')

                # 判断多个空格时
                if '    ' in x:
                    # 替换为空
                    x = x.replace('    ', '')

                # sql语句添加分号结尾
                sql_item = x + ';'
                # print(sql_item)
                self.sql_execute(sql_item)
                # print("执行成功sql: %s" % sql_item)

if __name__ == '__main__':

    db = MonitorDB()
    sqlfilepath = "文件路径"
    db.sql_execute_file(sqlfilepath)
    res =  db.sql_execute()
    # if res:
