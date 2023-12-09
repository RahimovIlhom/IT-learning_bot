import psycopg2

from data.config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class Database:
    def __init__(self):
        self.db = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.db.autocommit = True

    @property
    def connect(self):
        return self.db

    def select_categories(self):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_category;
        """
        cur.execute(sql_query)
        resp = cur.fetchall()
        return resp

    def select_sub_categories(self):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_subcategory;
        """
        cur.execute(sql_query)
        resp = cur.fetchall()
        return resp

    def select_sub_categories_in(self, category_id):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_subcategory where category_id=%s;
        """
        cur.execute(sql_query, (category_id, ))
        resp = cur.fetchall()
        return resp

    def select_lessons(self):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_lesson;
        """
        cur.execute(sql_query)
        resp = cur.fetchall()
        return resp

    def select_sub_category_lessons(self, subcategory_id):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_lesson where sub_category_id=%s;
        """
        cur.execute(sql_query, (subcategory_id, ))
        resp = cur.fetchall()
        return resp

    def select_lesson(self, lesson_id):
        conn = self.connect
        cur = conn.cursor()
        sql_query = """
            select * from bot_lesson where id=%s;
        """
        cur.execute(sql_query, (lesson_id,))
        resp = cur.fetchone()
        return resp
