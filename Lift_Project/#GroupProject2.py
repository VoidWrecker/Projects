import math
import matplotlib.pyplot as plt
import numpy as np
#Function 1
import csv
time=[]
fx=[]
fy=[]
fz=[]
f=[]
mx=[]
my=[]
mz=[]
b=[]
with open (r'C:\Users\andre\Documents\UCCS Schoolwork (temp)\misc\\shoulder_lifting_10kg_data.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)
    next(csv_reader)
    for line in csv_reader:
        time.append(float(line[0]))
        fx.append(float(line[1]))
        fy.append(float(line[2]))
        fz.append(float(line[3]))
        f.append(float(line[4]))
        mx.append(float(line[5]))
        my.append(float(line[6]))
        mz.append(float(line[7]))
        b.append((float(line[4])/101)*100)

#Function 2

#First graph Force over time
plt.plot(time,f)
plt.ylabel("Force(N)")
plt.xlabel("Time (s)")
plt.title("Force Over Time")

#Indices of vertical lines
#[ 258 871 966 1474 1748 1956 ]#

#initial hold
plt.axvline(x=time[258],ls="--")

#second hold
plt.axvline(x=time[871],ls="--")
plt.axvline(x=time[966],ls="--")

#third hold
plt.axvline(x=time[1474],ls="--")
plt.axvline(x=time[1748],ls="--")

#end of data
plt.axvline(x=time[1956],ls="--")

plt.show()

#Second graph force over time adjusted
t1=time[258]-time[0]
t2=time[966]-time[871]  
t3=time[1748]-time[1474]
    #Removing excess data

print(t1,t2,t3)
timea=time
fa=f
ba=b
   
del timea[1956:(len(time)-1)]
del fa[1956:(len(f)-1)]
del ba[1956:(len(b)-1)]

del timea[1474:1748]
del fa[1474:1748]
del ba[1474:1748]

del timea[871:966]
del fa[871:966]
del ba[871:966]

del timea[0:258]
del fa[0:258]
del ba[0:258]


plt.plot(timea,fa)
plt.ylabel("Force(N)")
plt.xlabel("Time (s)")
plt.title("Altered Force Over Time")

plt.show()



#Third Graph B over time
plt.plot(timea,ba)
plt.ylabel("%B")
plt.xlabel("Time (s)")
plt.title("Altered %B Over Time")

plt.show()
print(len(time))

#Function 3
import numpy as np

#first hold
fxavg1=np.average(fx[0:258])
fyavg1=np.average(fy[0:258])
fzavg1=np.average(fz[0:258])
#t1=time[258]-time[0]

#second hold
fxavg2=np.average(fx[871:966])
fyavg2=np.average(fy[871:966])
fzavg2=np.average(fz[871:966])
#t2=time[966]-time[871]

#third hold
fxavg3=np.average(fx[1474:1748])
fyavg3=np.average(fy[1474:1748])
fzavg3=np.average(fz[1474:1748])
#t3=time[1748]-time[1474]

#function 4
#assigning lifts
time_lift1 = timea[0:612]
time_lift2 = timea[613:1121]
time_lift3 = timea[1122:len(timea)]

#finding new times
time_subtract1 = time_lift1[0]
time_lift1new = [round(x - time_subtract1, 3) for x in time_lift1]
time_subtract2 = time_lift2[0]
time_lift2new = [round(x - time_subtract2, 3) for x in time_lift2]
time_subtract3 = time_lift3[0]
time_lift3new = [round(x - time_subtract3, 3) for x in time_lift3]

#finding max force in each direction
forcex_max1 = max(fx[259:870])
forcex_final1 = round(forcex_max1 - fxavg1, 3)
forcey_max1 = max(fy[259:870])
forcey_final1 = round(forcey_max1 - fyavg1, 3)
forcez_max1 = max(fz[259:870])
forcez_final1 = round(forcez_max1 - fzavg1, 3)
forcex_max2 = max(fx[967:1473])
forcex_final2 = round(forcex_max2 - fxavg2, 3)
forcey_max2 = max(fy[967:1473])
forcey_final2 = round(forcey_max2 - fyavg2, 3)
forcez_max2 = max(fz[967:1473])
forcez_final2 = round(forcez_max2 - fzavg2, 3)
force_mag1 = round(math.sqrt((forcex_final1 ** 2)+ (forcey_final1 ** 2) + (forcez_final1 ** 2)), 3)
force_mag2 = round(math.sqrt((forcex_final2 ** 2)+ (forcey_final2 ** 2) + (forcez_final2 ** 2)), 3)

#function 5

fx1 = fx[258:870]
fy1 = fy[258:870]
fz1 = fz[258:870]
f1 = f[0:612]
fx2 = fx[966:1474]
fy2 = fy[966:1474]
fz2 = fz[966:1474]
f2 = f[0:508]

#first plot
fig, axs = plt.subplots(2)
axs[0].plot(time_lift1new, fx1, color='green')
axs[0].plot(time_lift1new, fy1, color='blue')
axs[0].plot(time_lift1new, fz1, color ='red')
axs[0].plot(time_lift1new, f1, color='black')
axs[0].set_title("Altered Force Over Time For First Lift")
axs[0].legend(['Fx', 'Fy', 'Fz', 'F'])

#second Plot
axs[1].plot(time_lift2new, fx2, color='green')
axs[1].plot(time_lift2new, fy2, color='blue')
axs[1].plot(time_lift2new, fz2, color ='red')
axs[1].plot(time_lift2new, f2, color='black')
axs[1].set_title("Altered Force Over Time For Second Lift")
axs[1].legend(['Fx', 'Fy', 'Fz', 'F'])

fig.supylabel("Force (N)")
fig.supxlabel("Time (s)")
fig.tight_layout()

plt.show()




print("")
print("The first hold lasted %f seconds with an average force of %f in the x direction, %f in the y direction, and %f in the z direction."%(t1,fxavg1,fyavg1,fzavg1))
print("")
print("The second hold lasted %f seconds with an average force of %f in the x direction, %f in the y direction, and %f in the z direction."%(t2,fxavg2,fyavg2,fzavg2))
print("")
print("The third hold lasted %f seconds with an average force of %f in the x direction, %f in the y direction, and %f in the z direction."%(t3,fxavg3,fyavg3,fzavg1))
print("")
print("The start time for the first lift was ", time_lift1[0], "seconds and the end time for the first lift was ", time_lift1[len(time_lift1) - 1], "seconds.")
print("")
print("The maximum force magnitute for the first lift was ", force_mag1, "Newtons.")
print("")
print("The start time for the second lift was ", time_lift2[0], "seconds and the end time for the second lift was ", time_lift2[len(time_lift2) - 1], "seconds.")
print("")
print("The maximum force magnitute for the second lift was ", force_mag2, "Newtons.")