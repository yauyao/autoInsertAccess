import pyodbc

def connectAccess():
    DBfile = "E:\CIS-PC.accdb"  # Access檔案所在地
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile+';')  #連結DateBase

    cursor = conn.cursor()
    SQL = "SELECT * from cis;"  # 僅範例參考
    for row in cursor.execute(SQL):
        print(row[1])

    cursor.close()  #關閉連線


if __name__ == '__main__':
    connectAccess()