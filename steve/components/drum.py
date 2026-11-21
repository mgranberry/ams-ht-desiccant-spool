import cadquery as cq
from math import cos, sin, radians
from retention import bayonet_angles, sector, profiled_sector
from ports import tracks
from steve import Component
from geometry import build_fill_half, build_discharge_half

lower = build_fill_half()
lower = lower.cut(cq.Solid.makeBox(204,204,4,cq.Vector(-102,-102,-1)))
upper = build_discharge_half().rotate((0,0,0),(1,0,0),180).translate((0,0,60))
drum = Component("drum", name="One-piece perforated drum")
# The nozzle crosses the original modeling seam. Clear the bore after joining.
throat = cq.Solid.makeCylinder(8.05,10.5,cq.Vector(87.65,0,22.5),cq.Vector(1,0,0))
peak = (cq.Workplane("YZ",origin=(86.9,0,22.5))
    .polyline([(-6,-5),(6,-5),(0,-11.4)]).close().extrude(10).val())
body = lower.fuse(upper).cut(throat,peak)
# A recessed straight nose gives the container a locating surface.
axis = cq.Vector(1,0,0)
nose = cq.Solid.makeCylinder(14.5,7.3,cq.Vector(91.5,0,22.5),axis)
root_clearance = cq.Solid.makeCylinder(11.9,5,cq.Vector(91.4,0,22.5),axis)
plug_recess = cq.Solid.makeCylinder(13.3,3.0,cq.Vector(96,0,22.5),axis)
# Grow the projection at 45 degrees from the previously printed shoulder.
ramp_limit = (cq.Workplane("XZ").polyline([(90,5),(99,5),(99,31),(90,40)])
    .close().extrude(16,both=True).val())
collar = nose.cut(root_clearance,plug_recess).intersect(ramp_limit)
# Keep the existing flange seat and trim bulky material around the nose.
neck_zone = cq.Solid.makeBox(9,44,38,cq.Vector(91.5,-22,4))
body = body.cut(neck_zone.cut(nose)).fuse(collar)
socket_cuts = [cut.rotate((0,0,0),(0,1,0),-90).translate((96,0,22.5)) for cut in tracks(8)]
# A continuous collar supplies the shoulders at the junction of the collector halves.
socket_base = cq.Vector(89,0,22.5)
sleeve = cq.Solid.makeCylinder(10.15,7, socket_base,axis).cut(
    cq.Solid.makeCylinder(8.05,7.4,cq.Vector(88.8,0,22.5),axis),peak)
body = body.fuse(sleeve).cut(*socket_cuts).clean()
for angle in bayonet_angles:
    receiver = profiled_sector([(85.4,3),(90.4,3),(90.4,16),(89.4,16),(85.4,12)],angle-7,24)
    entry = sector(85.2,89.55,2.9,6,angle-4.5,9)
    track = sector(85.2,89.55,5.4,3.2,angle-4.5,17.25)
    a = radians(angle+5.8)
    detent = cq.Solid.makeCylinder(1.05,3.25,cq.Vector(89.75*cos(a),89.75*sin(a),5.38))
    receiver = receiver.cut(entry,track).fuse(detent)
    body = body.fuse(receiver)
# One tick for insertion, a close pair for locked, viewed across the lid seam.
for tick in (81,90,92):
    notch = cq.Solid.makeBox(1,1.3,3,cq.Vector(90.35,-0.65,3))
    body = body.cut(notch.rotate((0,0,0),(0,0,1),tick))
# Open opposite sides of the outlet recess down behind the plug flange.
for side in (-1,1):
    access = cq.Solid.makeBox(6,10,38,cq.Vector(94.5,10.4 if side > 0 else -20.4,4))
    body = body.cut(access)
drum.add("solid", cq.Workplane(obj=body.clean()))
