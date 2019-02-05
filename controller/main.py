from service.access.insertAccess import connectAccess,executeSql,closeAccess,searchSql
from service.webCrawler.crawler import printDatePrice
import datetime

if __name__ == '__main__':
    con = connectAccess()
    result = searchSql("select cis_id,base_info from cis order by cis_id",con)

    content = result[0]
    for content in result:
        print("id:%d url:%s" % (content[0],content[1]))
        list = printDatePrice(content[1])

        search = searchSql("select cis_date from cis_log where cis_id =%d ORDER BY cis_date desc" % content[0],con)

        print("Last Date: %s" % search[0][0])

        for element in list:
            datetime_obj = datetime.datetime.strptime(element._date, '%Y/%m/%d')
            if search[0][0] < datetime_obj:
                insertSql = "insert into cis_log (cis_date,unit_price,cis_id) VALUES ('%s',%f,%s);" % (element._date,float(element._price),content[0])
                print("     %s" % insertSql)
                executeSql(insertSql, con)
            else:
                print("     have data:%s" % element._date)


    closeAccess(con)