from service.access.insertAccess import connectAccess,executeSql,closeAccess

if __name__ == '__main__':
    con = connectAccess()
    result = executeSql("select base_info from cis",con)
    closeAccess(con)

    for content in result:
        print("url:" + content[0])