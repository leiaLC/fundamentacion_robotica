import roboticstoolbox as rtb
import numpy as np

panda = rtb.models.ETS.Panda()

#qr is the angular position by default
print("Defalt angular position qr")
print(panda.qr)
print("Homogeneous Transformation Matrix")
print(panda.fkine(panda.qr))

#D-H parameters
panda_dh = rtb.models.DH.Panda()
print(panda_dh)

#Plot Robot
panda.plot(panda.qr, block = True)

#Plot new position
new_pos = np.array([0, 0, 0, 0, 0, 0, 0])
panda.plot(new_pos, block = True)
print(panda.fkine(new_pos))