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
        bump = cq.Solid.makeCylinder(0.48 if radius == 28 else 0.58,3.5,
            cq.Vector((radius+1.60)*cos(a),(radius+1.60)*sin(a),3.4))
        cuts.append(track.cut(bump))
    return cuts

def port_plug(radius,head_radius):
    shaft_clearance = 0.55 if radius == 28 else 0.35
    shaft = cq.Solid.makeCylinder(radius-shaft_clearance,7,cq.Vector(0,0,1.9))
    head = cq.Solid.makeCylinder(head_radius,2)
    half = degrees(2.0/radius)
    lugs = [profiled_sector([(radius-0.55,6),(radius-0.3,6),
                             (radius+1.15,7.5),(radius+1.15,8.3),
                             (radius-0.55,8.3)], a-half,2*half)
            for a in starts(radius)]
    if radius == 28:
        head = cq.Solid.makeCylinder(head_radius,7,cq.Vector(0,0,-5))
        pockets = [cq.Workplane("XY",origin=(0,y,-5.1)).slot2D(34,9)
                   .extrude(5.3).val() for y in (-7.5,7.5)]
        # A 6 mm web between the pockets gives fingers a grip for twist and pull.
        head = head.cut(*pockets)
    return head.fuse(shaft,*lugs).clean()
