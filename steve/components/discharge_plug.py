import cadquery as cq
from steve import Component
from ports import port_plug, turn

discharge_plug = Component("discharge_plug", name="Discharge bayonet plug")
locked = port_plug(8,13).rotate((0,0,0),(0,0,1),turn)
discharge_plug.add("solid", cq.Workplane(obj=locked))
