import cadquery as cq
from math import hypot
from ports import tracks
from steve import Component
from retention import bayonet_angles, sector, profiled_sector

vent_width = 1.2
def cylinder(r,h,z=0):
    return cq.Solid.makeCylinder(r,h,cq.Vector(0,0,z))

disk = cylinder(100,3)
collar = cylinder(32.2,8.2)
cone = cq.Solid.makeCone(30,14,16,cq.Vector(0,0,8))
bore = cylinder(28,9,-1).fuse(cq.Solid.makeCone(28,12,16.001,cq.Vector(0,0,8)))
cuts = [bore, *tracks(28)]
for x in range(-76,31,5):
    for y in range(-72,73,12):
        if hypot(max(abs(x)-0.6,0),max(abs(y)-4,0))<35 or hypot(abs(x)+0.6,abs(y)+4)>82:
            continue
        cuts.append(cq.Solid.makeBox(vent_width,8,4,cq.Vector(x-0.6,y-4,-0.5)))
# Lugs travel along the tracks and seat behind the retaining shoulders.
tabs = []
for angle in bayonet_angles:
    stem = sector(82.5,85.15,2.8,5.4,angle-2.5,5)
    lug = profiled_sector([(84.9,5.8),(86.5,5.8),(88.9,8.2),(84.9,8.2)],angle-2.5,5)
    tabs.append(stem.fuse(lug))
# Index on the drum-facing flange, outside the bayonet and inside the roller track.
index = cq.Solid.makeBox(8,1.4,0.7,cq.Vector(90,-0.7,2.4)).rotate((0,0,0),(0,0,1),81)
cuts.append(index)
lid = Component("lid", name="Flat bayonet-lock fill lid")
lid.add("solid", cq.Workplane(obj=disk.fuse(collar,cone,*tabs).cut(*cuts).clean()))
