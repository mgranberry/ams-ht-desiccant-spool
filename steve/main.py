from steve import Design, section_view
from components.drum import drum
from components.lid import lid
from components.fill_plug import fill_plug
from components.discharge_plug import discharge_plug

section_view("funnel_section", axis="y", at=0)
design = Design()
design.add(drum)
design.add(lid, at=((0,0,0),("Z",10)))
design.add(fill_plug, at=((0,0,-2),("Z",10)))
design.add(discharge_plug, at=((98,0,22.5),("Y",-90)))
result = design.result()
