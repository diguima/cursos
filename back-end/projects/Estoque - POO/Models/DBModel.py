import sqlite3


class DB:

    def __init__(self, bd):

        self.__conn = sqlite3.connect(bd)
        self.__cursor = self.__conn.cursor()

    def create_table(self, table, columns):
            
        try:

            key = ''

            for col in columns:

                key += f'{col} {columns[col]}, '

            query = f'''
                CREATE TABLE IF NOT EXISTS {table} (
                {key[:-2]})
            '''

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True
            
        except Exception as e:

            return e

    def get_all(self, table):

        self.__conn.execute(f'''
            SELECT  * from {table}
        ''')

        return self.__cursor.fetchall()

    def insert_values(self, table, values):

        try:

            key = value = ''

            for val in values:

                key += f'{val}, '
                value += f'"{values[val]}", '

            query = f'INSERT INTO {table} ({key[:-2]}) VALUES ({value[:-2]})'

            print(query)

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True

        except Exception as e:

            return e

    def update_values(self, table, values, condition):

        try:

            key = where = ''

            for val in values:

                key += f'{val} = "{values[val]}"'

            for cond in condition:

                where += f'WHERE {condition[cond]}' if cond == 'where' else ''

            query = f'UPDATE {table} SET ({key[:-2]}) ({where})'

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True

        except Exception as e:

            return e

    def delete_values(self, table, condition):

        try:

            where = ''

            for cond in condition:

                where += f'WHERE {condition[cond]}' if cond == 'where' else ''

            query = f'DELETE FROM {table} ({where})'

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True

        except Exception as e:

            return e
