sec = int(input('tempo de duração em segundos:\n'))
hour = sec//(60*60)
minutes = (sec-(hour*3600))//60
seconds = sec-((hour*(60**2))+(minutes*60))
print ('{}:{}:{}'.format(hour, minutes, seconds))
