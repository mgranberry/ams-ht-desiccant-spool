import cadquery as cq
from math import hypot

def build_fill_half():
    inlet = True
    pitch = 4.0
    clearance = 0.30
    vent_width = 1.2
    screen_wall = 1.8  # mm, four 0.45 mm extrusion lines

    def cylinder(radius, height, z=0, x=0, y=0):
        return cq.Solid.makeCylinder(radius, height, cq.Vector(x,y,z))

    def rib(radius, z, height, depth, half_width):
        helix = cq.Wire.makeHelix(pitch, height, radius, center=cq.Vector(0,0,z))
        return (cq.Workplane("XZ").polyline([
            (radius-0.35,z-half_width), (radius+depth,z-0.27),
            (radius+depth,z+0.27), (radius-0.35,z+half_width)
        ]).close().sweep(helix,isFrenet=True).val())

    def frustum(bottom, top, height, z):
        return cq.Solid.makeCone(bottom,top,height,cq.Vector(0,0,z))
    bosses = []
    # Restore the rounded barrel and fill the space below the collector.
    barrel = cylinder(91,28,2)
    wall = barrel.cut(cylinder(91-screen_wall,29,2))
    # Cross sections of the continuous collector, measured from the nozzle tip.
    # Each pair is the ellipse's axial and tangential semiaxis in mm.
    collector_sections = [
        (7.9, 8, 8), (20, 11, 11), (30, 21, 33),
        (41, 42, 66), (52, 71, 92), (63, 107, 132),
    ]
    def at_outlet(shape):
        return shape.rotate((0,0,0),(0,1,0),-90).translate((96,0,37.5))

    def collector_profile(offset=0):
        profile = cq.Workplane("XY")
        previous = 0
        for depth, axial, tangential in collector_sections:
            profile = profile.workplane(offset=depth-previous).ellipse(axial+offset,tangential+offset)
            previous = depth
        shape = at_outlet(profile.loft(ruled=False).val()).translate((offset,0,0))
        if inlet:
            shape = shape.rotate((0,0,0),(1,0,0),180).translate((0,0,60))
        return shape

    void = collector_profile()
    outer = collector_profile(2.0)
    collector_zone = cq.Solid.makeBox(64,182,28,cq.Vector(36,-91,2))
    clip = cq.Solid.makeBox(115,250,53,cq.Vector(0,-125,3))
    void = void.intersect(clip)
    floor = barrel.intersect(collector_zone).intersect(outer).cut(void)
    wall = wall.cut(collector_zone).fuse(wall.intersect(collector_zone).intersect(outer))
    fins = [cq.Solid.makeBox(17,2,28,cq.Vector(73,-1,2))
            .rotate((0,0,0),(0,0,1),a) for a in (110,160,200,250)]
    body = cylinder(100,3).fuse(wall,floor,*fins,
        *[cylinder(5,30,0,x,y) for x,y in bosses])
    if inlet:
        tools = []
    else:
        # The outer collar sits within the roller envelope. The mouth opens into
        # the collector floor and converges toward the threaded radial outlet.
        body = body.fuse(at_outlet(frustum(11.5,13,16,0)))
        bore = cylinder(8,9,-1).fuse(frustum(8,13,18,8),cylinder(13,17,26))
        tools = [at_outlet(bore)]
    for x,y in bosses:
        if inlet:
            tools.extend([cylinder(1.7,32,-1,x,y),cylinder(3.2,3.1,-0.1,x,y)])
        else:
            tools.append(cylinder(1.3,13,18,x,y))
    # Integral cylindrical screen. Solid bands tie the two rows of slots together.
    for z, phase in ((3.8,0),(16,1)):
        for angle in range(0,360,2):
            a = angle + phase
            # Protect the fastener bosses, fin roots and the discharge ramp.
            if abs((a+45)%90-45)>6 and all(abs(a-fin)>4 for fin in (75,110,145,160,200,215,250,285)):
                if min(a,360-a)>57:
                    slot = cq.Solid.makeBox(9,vent_width,11,cq.Vector(84,-vent_width/2,z))
                    tools.append(slot.rotate((0,0,0),(0,0,1),a))
    # Axial airflow through the two end plates. Keep vents out of the collector.
    for x in range(-76,58,5):
        for y in range(-72,73,12):
            near = hypot(max(abs(x)-vent_width/2,0),max(abs(y)-4,0))
            far = hypot(abs(x)+vent_width/2,abs(y)+4)
            if (inlet and near < 35) or far > 82 or x > 30:
                continue
            if any(hypot(max(abs(x-bx)-vent_width/2,0),max(abs(y-by)-4,0))<7
                   for bx,by in bosses):
                continue
            tools.append(cq.Solid.makeBox(vent_width,8,4,
                cq.Vector(x-vent_width/2,y-4,-0.5)))
    # Vent the exposed collector while preserving the seam and outlet boss.
    for y in range(-60,61,5):
        for z in (6,11,16,21,26):
            if abs(abs(y)-24)<7 or hypot(y,z-(22.5 if inlet else 37.5))<16:
                continue
            tools.append(cq.Solid.makeCylinder(0.6,65,cq.Vector(34,y,z),cq.Vector(1,0,0)))
    solid = body.cut(*tools).clean()
    return solid

def build_discharge_half():
    inlet = False
    pitch = 4.0
    clearance = 0.30
    vent_width = 1.2
    screen_wall = 1.8  # mm, four 0.45 mm extrusion lines

    def cylinder(radius, height, z=0, x=0, y=0):
        return cq.Solid.makeCylinder(radius, height, cq.Vector(x,y,z))

    def rib(radius, z, height, depth, half_width):
        helix = cq.Wire.makeHelix(pitch, height, radius, center=cq.Vector(0,0,z))
        return (cq.Workplane("XZ").polyline([
            (radius-0.35,z-half_width), (radius+depth,z-0.27),
            (radius+depth,z+0.27), (radius-0.35,z+half_width)
        ]).close().sweep(helix,isFrenet=True).val())

    def frustum(bottom, top, height, z):
        return cq.Solid.makeCone(bottom,top,height,cq.Vector(0,0,z))
    bosses = []
    # Restore the rounded barrel and fill the space below the collector.
    barrel = cylinder(91,28,2)
    wall = barrel.cut(cylinder(91-screen_wall,29,2))
    # Cross sections of the continuous collector, measured from the nozzle tip.
    # Each pair is the ellipse's axial and tangential semiaxis in mm.
    collector_sections = [
        (7.9, 8, 8), (20, 11, 11), (30, 21, 33),
        (41, 42, 66), (52, 71, 92), (63, 107, 132),
    ]
    def at_outlet(shape):
        return shape.rotate((0,0,0),(0,1,0),-90).translate((96,0,37.5))

    def collector_profile(offset=0):
        profile = cq.Workplane("XY")
        previous = 0
        for depth, axial, tangential in collector_sections:
            profile = profile.workplane(offset=depth-previous).ellipse(axial+offset,tangential+offset)
            previous = depth
        shape = at_outlet(profile.loft(ruled=False).val()).translate((offset,0,0))
        if inlet:
            shape = shape.rotate((0,0,0),(1,0,0),180).translate((0,0,60))
        return shape

    void = collector_profile()
    outer = collector_profile(2.0)
    collector_zone = cq.Solid.makeBox(64,182,28,cq.Vector(36,-91,2))
    clip = cq.Solid.makeBox(115,250,53,cq.Vector(0,-125,3))
    void = void.intersect(clip)
    floor = barrel.intersect(collector_zone).intersect(outer).cut(void)
    wall = wall.cut(collector_zone).fuse(wall.intersect(collector_zone).intersect(outer))
    fins = [cq.Solid.makeBox(17,2,28,cq.Vector(73,-1,2))
            .rotate((0,0,0),(0,0,1),a) for a in (110,160,200,250)]
    body = cylinder(100,3).fuse(wall,floor,*fins,
        *[cylinder(5,30,0,x,y) for x,y in bosses])
    if inlet:
        tools = []
    else:
        # The outer collar sits within the roller envelope. The mouth opens into
        # the collector floor and converges toward the threaded radial outlet.
        # Print from the fixed face. This permanent corbel grows 1 mm outward
        # per millimetre of height and stops short of the container-lip gap.
        corbel = (cq.Workplane("XZ").polyline([(59,2),(72,2),(96,26),(96,37.5),(74,38)])
            .close().extrude(12,both=True).val())
        # The peaked roof prints upward from the horizontal bore.
        roof = (cq.Workplane("YZ",origin=(73,0,37.5))
            .polyline([(-9,4),(9,4),(0,13)]).close().extrude(23).val())
        body = body.fuse(corbel,roof,at_outlet(frustum(11.5,14,23,0)))
        throat = at_outlet(cylinder(8,9,-1))
        nozzle_entry = void.intersect(cq.Solid.makeBox(60,90,53,cq.Vector(53,-45,3)))
        tools = [throat,nozzle_entry]

    for x,y in bosses:
        if inlet:
            tools.extend([cylinder(1.7,32,-1,x,y),cylinder(3.2,3.1,-0.1,x,y)])
        else:
            tools.append(cylinder(1.3,13,18,x,y))
    # Integral cylindrical screen. Solid bands tie the two rows of slots together.
    for z, phase in ((3.8,0),(16,1)):
        for angle in range(0,360,2):
            a = angle + phase
            # Protect the fastener bosses, fin roots and the discharge ramp.
            if abs((a+45)%90-45)>6 and all(abs(a-fin)>4 for fin in (75,110,145,160,200,215,250,285)):
                if min(a,360-a)>57:
                    slot = cq.Solid.makeBox(9,vent_width,11,cq.Vector(84,-vent_width/2,z))
                    tools.append(slot.rotate((0,0,0),(0,0,1),a))
    # Axial airflow through the two end plates. Keep vents out of the collector.
    for x in range(-76,34,4):
        for y in range(-72,73,9):
            near = hypot(max(abs(x)-vent_width/2,0),max(abs(y)-4,0))
            far = hypot(abs(x)+vent_width/2,abs(y)+4)
            if (inlet and near < 35) or far > 82:
                continue
            if any(hypot(max(abs(x-bx)-vent_width/2,0),max(abs(y-by)-4,0))<7
                   for bx,by in bosses):
                continue
            tools.append(cq.Solid.makeBox(vent_width,8,4,
                cq.Vector(x-vent_width/2,y-4,-0.5)))
    # Vent the exposed collector while preserving the seam and outlet boss.
    for y in range(-60,61,5):
        for z in (6,11,16,21,26):
            if abs(abs(y)-24)<7 or hypot(y,z-(22.5 if inlet else 37.5))<16:
                continue
            tools.append(cq.Solid.makeCylinder(0.6,65,cq.Vector(34,y,z),cq.Vector(1,0,0)))
    solid = body.cut(*tools).clean()
    return solid
