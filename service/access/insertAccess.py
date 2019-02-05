import pyodbc

def connectAccess():
    DBfile = "E:\CIS-PC.accdb"  # Access檔案所在地
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % DBfile )  #連結DateBase

    return conn

def closeAccess(database):
    database.close()

def searchSql(sql,conn):
    cursor = conn.cursor()
    result = []
    for element in cursor.execute(sql):
        result.append(element)

    return result

def executeSql(sql,conn):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()



# if __name__ == '__main__':
#     con = connectAccess()
#     result = executeSql("select base_info from cis",con)
#     closeAccess(con)
#
#     for content in result:
#         print("url:" + content[0])