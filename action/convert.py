import re

def convert(response):
    responseDict = eval(response)
    if isinstance(responseDict,dict):
        for k in responseDict.keys():
            if k == "code":
                ResponseCode = responseDict[k]
            elif k == "msg":
                ResponseMessage = responseDict[k]
            else:
                ResponseData = responseDict[k]
        return ResponseCode,ResponseMessage,ResponseData
    else:
        return None


if __name__ == "__main__":
    print(convert('{"code":0,"msg":"Success.","data":{"me"}}'))