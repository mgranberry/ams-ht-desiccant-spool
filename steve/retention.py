"""Shared radial geometry for the lid bayonet."""
import cadquery as cq
bayonet_angles = (81,144,216,272)
lock_angle = 10

def sector(inner,outer,z,height,start,sweep):
    wedge = cq.Solid.makeCylinder(outer,height,cq.Vector(0,0,z),angleDegrees=sweep)
    bore = cq.Solid.makeCylinder(inner,height+2,cq.Vector(0,0,z-1))
    return wedge.cut(bore).rotate((0,0,0),(0,0,1),start)

def profiled_sector(profile,start,sweep):
    section = cq.Workplane("XZ").polyline(profile).close()
    return section.revolve(sweep,(0,0),(0,1)).val().rotate((0,0,0),(0,0,1),start)
