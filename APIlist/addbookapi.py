import logging
from utilities.configuration import *
from utilities import custom_logging as cl
from utilities.Resources import *
import requests
from utilities.payload import *


class AddBook:
    log = cl.log(logging.DEBUG)
    gquery = 'select * from Books'

    def validateaddbook(self):
        gurl = getconfig()['API']['endpoint']+Resources.addbookresource

        resol= requests.post(gurl, json= payloadadd(self.gquery))

        self.log.info(resol)
        res_json = resol.json()
        self.log.info(res_json)
        if res_json['Msg']=='successfully added' and res_json['ID'] is not None:
            return True
        else:
            return False

    # def validatemessage(self):
    #     aurl= getconfig()['API']['endpoint']+Resources.addbookresource
    #     #gquery = 'select * from Books'
    #     res= requests.post(aurl,json=payloadadd(self.gquery))
    #     self.log.info(res)
    #     res_json= res.json()
    #     self.log.info(res_json)
    #     if res_json['Msg'] == 'successfully added' and res_json['ID'] is not None:
    #         return True
    #     else:
    #         return False

    def updatebook(self):
        row = getquery(self.gquery)
        uquery = 'update Books set aisle = %s where Bookname = %s'

        data = (int(row[2])+1, row[0])
        updatequery(uquery,data)

    def getid(self):
        gurl = getconfig()['API']['endpoint'] + Resources.addbookresource
        res = requests.post(gurl, json=payloadadd(self.gquery))
        self.log.info(res)
        res_json = res.json()
        id = res_json['ID']
        return id

    def validatedelete(self):
        durl = getconfig()['API']['endpoint']+ Resources.deletebookresource
        id = self.getid()
        resp = requests.post(durl, json= payloaddelete(id))
        self.log.info(resp)
        resp_json = resp.json()
        if resp_json['msg']== 'book is successfully deleted':
            return True
        else:
            return False


