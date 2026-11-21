import cadquery as cq
from steve import Component
from ports import port_plug, turn

fill_plug = Component("fill_plug", name="Fill bayonet plug")
locked = port_plug(28,33).rotate((0,0,0),(0,0,1),turn)
fill_plug.add("solid", cq.Workplane(obj=locked))
