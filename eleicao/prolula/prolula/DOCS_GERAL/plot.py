import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('00h-02h', '02h-04h', '04h-06h', '06h-08h', '08h-10h', '10h-12h', '12h-14h', '14h-16h', '16h-18h', '18h-20h', '20h-22h', '22h-23:59h')
y_pos = np.arange(len(objects))
performance = [100,80,63,47,200,150,270,500,1000,650,750,300]
 
plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, objects)
plt.ylabel('Retweets')
plt.title('Quantidade de retweets Pró-lula')
 
plt.show()
