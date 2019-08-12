import re

response = {
    "code":0,
    "msg":"Success.",
    "data":{
        "shelfs":[
            {
                "shelfIndex":"1",
                "isVirtual":"false",
                "slots":[
                    {
                        "slotIndex":"1",
                        "isVacant":"false",
                        "boardType":"SCMIP2",
                        "hardwareVersion":"0206030157A1",
                        "firmwareVersion":"3.1",
                        "FPGAVersion":"4.1",
                        "serialNumber":"123456789",
                        "ports":[

                        ]
                    },
                    {
                        "slotIndex":"2",
                        "isVacant":"true",
                        "boardType":"FXS-24BT",
                        "hardwareVersion":"-",
                        "firmwareVersion":"-",
                        "FPGAVersion":"-",
                        "serialNumber":"-",
                        "ports":[
                            1,
                            2,
                            3,
                            4,
                            5,
                            6,
                            7,
                            8,
                            9,
                            10,
                            11,
                            12,
                            13,
                            14,
                            15,
                            16,
                            17,
                            18,
                            19,
                            20,
                            21,
                            22,
                            23,
                            24
                        ]
                    }
                ]
            }
        ]
    }
}

# print(str(response))

s = re.search(r"\'shelfs\':\s+\[(.*)\]",str(response),re.M|re.S)
print(s.group(1))