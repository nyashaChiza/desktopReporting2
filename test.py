def dateCheck1(value):
            result = []
            maps=[]
            value = str(value).split('/')
            print('date:',value)
            if len(value[0])==1:
                maps.append(1)
            else:
                maps.append(0)
            if len(value[1])== 1:
                maps.append(1)
            else:
                maps.append(0)
            if maps[0] ==1:
                       result.append('0')
            else:
                        result.append('')
            if maps[1] ==1:
                       result.append('0')
            else:
                        result.append('')
            return result[0]+value[0]+result[1]+value[1]+value[2]
print(dateCheck1('1/12/2015'))