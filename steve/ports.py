"""Two-lug bayonets. Z points from the outside face into the chamber."""
import cadquery as cq
from math import radians, degrees, sin, cos
from retention import sector, profiled_sector

turn = 45
def starts(radius):
    return (55,235) if radius == 8 else (90,270)

def tracks(radius):
    half = degrees(2.0/radius)
    margin = degrees(0.35/radius)
    cuts = []
    for start in starts(radius):
        cuts.append(sector(radius-1,radius+1.55,-0.2,6.9,
                           start-half-margin,2*(half+margin)))
        track = sector(radius-1,radius+1.55,3.6,3.1,
                       start-half-margin,turn+2*(half+margin))
        # Leave a shallow bump on the track wall just before the locked position.
        a = radians(start+turn-half-degrees(1.0/radius))
        bump = cq.Solid.makeCylinder(0.58,3.5,
            cq.Vector((radius+1.60)*cos(a),(radius+1.60)*sin(a),3.4))
        cuts.append(track.cut(bump))
    return cuts

def port_plug(radius,head_radius):
    shaft = cq.Solid.makeCylinder(radius-0.35,7,cq.Vector(0,0,1.9))
    head = cq.Solid.makeCylinder(head_radius,2)
    half = degrees(2.0/radius)
    lugs = [profiled_sector([(radius-0.55,6),(radius-0.3,6),
                             (radius+1.15,7.5),(radius+1.15,8.3),
                             (radius-0.55,8.3)], a-half,2*half)
            for a in starts(radius)]
    drive = cq.Solid.makeBox(14,2.5,1,cq.Vector(-7,-1.25,-0.01))
    return head.fuse(shaft,*lugs).cut(drive).clean()
