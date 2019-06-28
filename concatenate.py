def concatenateSequence(*args,seperator):
    string = seperator.join(args)
    return string

def concatenateMapping(seperator,**kwargs):
    print(kwargs)
    string = seperator.join("{0}:{1}".format(i,kwargs.get(i)) for i in kwargs)
    return string

''' 시퀀스 패킹 언패킹 '''
print(concatenateSequence(*'일월화수목금토일',seperator=' - '))

''' 매핑 패킹 언패킹 방법 1 '''
myDict = {'gerrard':'worldClass','bailey':'amatuer','SeongYongKi':'gookBbong','kanginLee':'wonderKid'}
print(concatenateMapping(**myDict,seperator='\n'))

''' 매핑 패킹 언패킹 방법 2 '''
#print(concatenateMapping(gerrard='worldClass',bailey='amatuer',SeongYongKi='gookBbong',kanginLee='wonderKid',seperator='\n'))
