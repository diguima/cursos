import sqlite3
import lib.screen as screen 

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
                

    def get_sum(self, table, sum):

        query = f'''
            SELECT SUM({sum})
            FROM {table}      
        '''
        result = 0

        if self.__cursor.execute(query):

            recordsList = self.__cursor.fetchone()

            result = recordsList[0]

        return result
    
    def get_conditional_list(self, table, condition):

        where = ''

        for cond in condition:

            where += f'WHERE {condition[cond]}' if cond == 'where' else ''        

        query = f'''
            SELECT * FROM {table} {where}
        '''
        
        self.__cursor.execute(query)

        return self.__cursor.fetchall()
    
    def get_all(self, table):

        query = f'''
            SELECT * FROM {table}
        '''
        self.__cursor.execute(query)

        return self.__cursor.fetchall()
    
    def get_value_id(self, table, id):

        self.__cursor.execute(f'''
            SELECT * FROM {table} WHERE id = "{id}"
        ''')

        return self.__cursor.fetchall()    

    def insert_values(self, table, values):

        try:

            key = value = ''

            for val in values:

                key += f'{val}, '
                value += f'"{values[val]}", '

            query = f'INSERT INTO {table} ({key[:-2]}) VALUES ({value[:-2]})'

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True

        except Exception as e:

            return e

    def update_values(self, table, values, condition):

        try:

            key = where = ''

            for val in values:

                key += f'{val} = "{values[val]}", '

            for cond in condition:

                where += f'WHERE {condition[cond]}' if cond == 'where' else ''

            query = f'UPDATE {table} SET {key[:-2]} {where}'

            # print(values)
            # print(condition)
            # print(query)

            # screen.pause_screen()

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

            query = f'DELETE FROM {table} {where}'

            if self.__cursor.execute(query):

                self.__conn.commit()

                return True

        except Exception as e:

            return e
