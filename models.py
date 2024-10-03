from connectdb import mydb, mycursor
from utilities import filter_input, format_name

class Model:
    """Generic Model class to be used as a parent for any class/table for our application"""

    def __init__(self, table, columns):
        self.table  = table
        self.columns = columns

    #table getter
    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    #columns getter
    @property
    def columns(self):
        return self.__columns

    #column setter
    @columns.setter
    def columns(self, value):
        self.__columns = value

    def insert(self):
        columns = tuple(f"`{column}`" for column in self.columns)
        placeholders = tuple("%s" for _ in self.columns)
        sql = f"INSERT INTO `{self.table}` ("
        sql += ", ".join(columns)
        sql += f") VALUES ({", ".join(placeholders)})"
        values = tuple(getattr(self, column) for column in self.columns)
        mycursor.execute(sql, values)
        mydb.commit()

    def update(self, row_id):
        assignments = tuple(column + " = %s" for column in self.columns)
        sql =  f"UPDATE `{self.table}` SET "
        sql += ", ".join(assignments)
        sql += " WHERE id = %s"
        values = tuple(getattr(self, column) for column in self.columns) + (row_id,)
        mycursor.execute(sql, values)
        mydb.commit()

    def save(self, row_id=None):
        if row_id:
            self.update(row_id)
        else:
            self.insert()

    def delete(self, row_id):
        sql = f"DELETE FROM `{self.table}` WHERE id = {row_id}"
        mycursor.execute(sql)
        mydb.commit()

    def get_all(self):
        sql = f"SELECT * FROM `{self.table}`"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def get(self, row_id):
        sql = f"SELECT * FROM `{self.table}` WHERE id = {row_id}"
        mycursor.execute(sql)
        return mycursor.fetchone()

class Animal(Model):
    """This is a child class of Model class for animals table in our app"""
    def __init__(self, form=None):
        table = "animals"
        columns = ("name", "image", "region", "predator")
        super().__init__(table, columns)

        if form:
            self.name = form.name.data
            self.image = form.image.data
            self.region = form.region.data
            self.predator = form.predator.data

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = format_name(value) 

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = filter_input(value, r"([^a-zA-Z0-9_\-.]+)") 

    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, value):
        self.__region = format_name(value) 

    @property
    def predator(self):
        return self.__predator
    
    @predator.setter
    def predator(self, value):
        self.__predator = value     
    
