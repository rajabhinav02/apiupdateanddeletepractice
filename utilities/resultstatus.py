import logging

from utilities import custom_logging as cl

class ResultStatus:
    log = cl.log(logging.DEBUG)
    resultlist= []

    def ResultS(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info(resultmessage + " working fine")
                else:
                    self.resultlist.append("Fail")
                    self.log.error(resultmessage+" not working")
            else:
                self.resultlist.append("Fail")
                self.log.error(resultmessage+ " not working")
        except:
            self.resultlist.append("Fail")
            self.log.error(resultmessage+ " not working")

    def marktest(self, result, resultmessage):
        self.ResultS(result, resultmessage)

    def marktestfinal(self, result, resultmessage, tcname):
        self.ResultS(result, resultmessage)

        if "Fail" in self.resultlist:
            self.log.error(tcname+ " Failed")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(tcname+ " Passed")
            self.resultlist.clear()
            assert True == True