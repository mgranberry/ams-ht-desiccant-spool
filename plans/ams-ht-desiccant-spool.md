# AMS-HT desiccant spool for STEVEcad

## Design envelope

All dimensions are nominal millimetres before ABS shrinkage. Model two drum halves and two removable plugs. The roller rims define a 200 mm diameter. The drum is 60 mm wide and the seated plug flanges bring the total width to 64 mm. Bambu specifies 197–202 mm diameter and 50–68 mm width. [AMS-HT specifications](https://cdn1.bambulab.com/documentation/h2d/en/AMS_HT_20250109.pdf)

Both funnels print integrally with their end plates. Removing a plug exposes its funnel.

## Geometry and construction order

Use the spool axis as Z. Build each half in its own coordinates with the outside face at Z = 0 and the mating face at Z = 30. In the assembly, flip the outlet half 180° about X and translate it 60 mm along Z.

| Feature | Nominal geometry for each half |
| --- | --- |
| Roller rim and end plate | Solid disc of radius 100 from Z = 0 to 3. Keep the outer circumference continuous. |
| Drum wall | Annulus with outer radius 91 and inner radius 88.5 extending from the plate to Z = 30. The two annular ends meet at the seam. |
| Fill funnel | Coaxial frustum with a 56 mm bore at Z = 8 narrowing to 24 mm at Z = 24. Add 2 mm radial wall thickness. Cut the bore through the end plate. |
| Discharge funnel | Reverse the bore taper, giving a 56 mm chamber-side mouth at Z = 24 and a 24 mm spout at Z = 8. Tilt and roll the drum to collect beads at the central opening. |
| Mixing fins | Four axial plates at 45°, 135°, 225° and 315°. Each spans radii 73–90, is 2 mm thick tangentially, and extends from Z = 2 to 26. Fuse the root to the wall and plate. Leave the fin tips open across the seam. |
| Fasteners | Four axial bosses of radius 5 on an 87 mm bolt circle **radius**, at 90° intervals starting on +X. Give the inlet bosses 3.4 mm through holes and 6.4 mm diameter counterbores 3 mm deep. Give the outlet bosses 2.6 mm pilots 12 mm deep from the seam. Use four M3 × 35 socket-head screws. |
| Face ventilation | Cut 1.2 × 10 slots through both plates on a 4 × 12 rectangular pitch. Orient the long axis along Y. Keep slot centres outside radius 37, slot corners inside radius 85, and a minimum 2 mm web beside each boss. Make slot width a parameter tied to the smallest retained bead. |
| Closures | Fuse a threaded collar from each end plate to its funnel at Z = 8. Use single-start right-hand threads, 4 mm pitch, 1.2 mm radial depth and 45° flanks. Female minor diameters are 56 mm for fill and 24 mm for discharge. Leave 3 mm of collar wall beyond the thread root. Give each plug a matching 7.5 mm threaded shank with a chamfered start and an initial 0.3 mm radial clearance. Use 2 mm seating flanges, 66 and 34 mm in diameter respectively, with recessed coin slots. |

## STEVEcad implementation and checks

Expose rim diameter, half depth, wall thickness, vent width, funnel diameters, fin reach and thread clearance as named dimensions. Build the shared half geometry once, selecting the funnel direction and fastener cuts per half. Provide individual part views in print orientation and an assembled section through the axis and two bosses.

Before printing the drum, section the assembly to verify open funnel throats, screw engagement and clearance between opposing fins. Slice both halves rim-down and plugs flange-down. Inspect the outlet funnel's expanding wall for unsupported layers. Test a vent coupon with the smallest beads and plug coupons after a heat cycle. Check the assembled rims for roundness and runout, then try a small partial load to confirm roller traction, tumbling, bead retention and discharge. Confirm the bead supplier's regeneration temperature is achievable within the AMS-HT's 85 °C limit.

## Built revision with low-point discharge

The STEVECad assembly uses a side fill plug and a discharge port offset 68 mm from the axis. Index the discharge port downward, remove its plug, and tip the spool roughly 65° from the operating position toward the outlet face. A broad sloping floor rises toward the cylindrical wall and feeds a 24 mm outlet through an asymmetric funnel cut into the ramp.

The cylindrical walls serve as printed screens. Each half has two staggered rows of 1.2 × 10 mm slots with solid bands between rows and solid sectors at the bosses and fin roots. The discharge half also retains a solid sector behind the ramp. The four axial fins per half still lift the beads during rotation.

Check emptying with a small bead load and check the effect of the off-axis ramp on roller traction. The slotted screen needs a sliced or printed coupon to verify bead retention.

## Screw-in pour spout

A fifth component replaces the discharge plug while emptying. It uses the same 4 mm-pitch thread and extends 39 mm from the end plate. The hollow body tapers from a 20.6 mm bore at the threaded inlet to a 15 mm clear tip opening. The tip is offset 7 mm from the thread axis so it can reach into a container. The CAD assembly shows the spout alongside the closed spool.

## ABS screen revision

The cylindrical screen is 1.8 mm thick, sized for four nominal 0.45 mm extrusion lines. Each half has two staggered rows of 1.2 × 11 mm slots at 2° pitch. The fill and discharge halves have 272 and 176 through-slots respectively. Solid bands support the rows, and unperforated sectors retain material at the screw bosses, fin roots, and ramp.

Slice both drum halves with their flat outer faces on the bed, both plugs flange-down, and the spout tip-down. Use an enclosed ABS print setup and inspect the sliced wall for continuous extrusion lines and the short bridges across the slots. Print a screen and thread coupon to confirm the slot width, ABS shrinkage, and plug engagement before committing to the full drum.

## Radial bottom outlet

The flattened barrel chord at X = 82 mm spans both halves. The circular 200 mm roller rims extend past the flat. Turn the flat to the six o'clock position with the spool axis horizontal. The sloped floor and side banks feed the integral radial funnel, which narrows to a 16 mm threaded bottom outlet. Use the screw plug during rotation. Attach the optional pour spout after lifting the spool over the receiving container.

Print the halves flat face down in ABS. Inspect the horizontal discharge bore and collar in the slicer and support the overhangs as needed. Make a radial port coupon to check support removal and thread fit. Test discharge from a horizontal axis and measure the residual beads before relying on complete drainage.

## End-face ventilation

Each circular end plate has 219 through-slots measuring 1.2 × 8 mm. The openings give air a path through the drum along its axis in addition to the cylindrical screen. The pattern preserves the roller rims, fastener seats, funnel areas, and collector floor. Compare bead regeneration at the same temperature, cycle time, and fill level to measure the benefit.

## Rounded-bottom assembly with integral pour nozzle

The current assembly has four printed components. The lower cylindrical wall is rounded, and the discharge half incorporates the collector, radial funnel and pour nozzle as one solid. The nozzle and seated plug fit inside the circular roller envelope. Position the outlet at six o'clock over the container and remove its plug to pour. The two plugs are the only parts removed during routine use.

Join the halves with four M3 × 35 mm socket-head cap screws, measured under the head. The fill half has 3.4 mm clearance holes and 6.4 mm diameter counterbores 3 mm deep. Tap the 2.6 mm pilots in the discharge half M3 × 0.5. The screws engage about 8 mm of the 12 mm pilot depth. M2 screws require resizing both clearance and pilot holes.

## Recessed collector and extended spout

The discharge half has a 42 mm-wide recess around the radial nozzle. A sealed bulkhead and side cheeks trade some bead capacity for 20 mm of exposed spout. The nozzle tip and screw plug stay within the roller rim diameter. The nozzle retains its 16 mm threaded opening. Inspect the recess-facing overhangs and horizontal bore for support access when slicing in ABS.

## Continuous collector surface

The current collector is generated from one family of elliptical cross-sections perpendicular to the radial outlet axis. From the nozzle tip inward, the sections are defined by the triples (depth, axial semiaxis, tangential semiaxis) in millimetres: (7.9, 8, 8), (20, 11, 11), (30, 21, 33), (41, 42, 66), (52, 71, 92), and (63, 107, 132). A smooth loft through these curves expands from the 16 mm nozzle bore into the drum. Both halves cut their collector from the same loft in assembly coordinates so the mating edges coincide. The mixing fins sit outside the collector.

## One-piece drum and removable lid

The drum, discharge face, perforated collector and pour nozzle print as one piece. The opposite circular face is a flat removable lid with the fill funnel projecting into the drum. Four tapered tabs locate the lid against solid areas of the drum, with 0.12 mm nominal radial interference. The assembly uses no screws. Both port plugs retain their coarse threads.

The collector follows the loft with a nominal 2 mm outward allowance. The old cylindrical backing is removed in that area. The collector and the circular discharge face are perforated where the shell can carry the openings. Slice the fixed discharge face down and check the internal hopper and radial nozzle for accessible support. Validate the lid fit with an ABS tab and wall coupon, including a heat cycle, before loading the drum.

The [collector section render](ams-collector-section.png) shows the final drum geometry with the plugs and lid removed. The outlet cut extends behind the nozzle root so the collector opens into the spout without a transverse ledge.

## Centered nozzle and bayonet lid

The nozzle axis is at Z = 32 mm in the 60 mm drum. The [nozzle section](ams-nozzle-clearance.png) shows a 12 mm-thick container lip reaching 14 mm into the gap beside the nozzle. A 30 mm-wide CAD gauge cleared the drum with the discharge plug removed.

Four lid lugs insert into matching axial slots. Rotate the lid 10° clockwise viewed from the fill side to seat the lugs under the retaining shoulders. Small detents resist reverse rotation. The CAD check found clearance at the insertion and locked positions. At 10° the shoulders block axial withdrawal. Check detent feel and retention on a printed ABS joint after a heat cycle.

## Collector seam and fixed-face ventilation

The cylindrical wall overlaps the start of the collector loft to close the unintended transition slit. The fixed face opposite the fill funnel uses a denser 4 × 9 mm pitch with 1.2 × 8 mm slots. The [drum render](ams-drum-ventilation.png) shows the fixed face and collector. The pattern keeps the roller rim and collector attachment solid.

## Support-free ABS print

The drum prints with the fixed perforated face down. The integral nozzle has a sloped underside and peaked bore. The nozzle center is now at Z = 22.5 mm. The 12 mm-thick, 30 mm-wide container-lip gauge still clears 14 mm into the gap. The four mixing fins run continuously through the former seam. The lid prints flange down, as do the two plugs. The bayonet lugs have sloped undersides and the detents grow out of the track walls.

Bambu Studio 2.9.1 sliced both projects with support disabled and no slicing warnings, using the X1 Carbon 0.4 mm nozzle, Bambu ABS, 0.20 mm layers, two wall loops, 15% infill and a textured PEI plate. The drum takes 124.43 g and the lid and plugs take 75.74 g, for 200.17 g total filament. The two brims account for about 1.63 g.

- [Sliced drum project](../print/ams-ht-drum-abs.3mf)
- [Sliced lid and plugs project](../print/ams-ht-lid-and-plugs-abs.3mf)

The [print-orientation section](ams-abs-print-section.png) shows the slope below the nozzle and the preserved container-lip gap.

## Straight pour lip

The outlet has a 29 mm outside diameter locating lip and a recessed seat for the existing screw plug. A 30 mm ID, 34 mm OD test opening clears 7.3 mm of straight insertion. The outer end sits at X = 98.8 mm and remains inside the roller envelope. The 45° underside starts behind the insertion area, and the side gap still accepts the 12 mm lip gauge. See the [outlet render](ams-pour-lip.png).

Bambu Studio resliced the drum with the prior ABS profile, supports off and no warnings. The revised drum estimate is 125.12 g. The two plates total 200.86 g including brims.

## Bayonet port closures

Revision 32 uses two-lug bayonets for both removable plugs. Turn either plug 45° clockwise from its entry position. The main lid uses a 10° turn with matching index marks. The current print projects, clearance checks, coupon plate, and remaining prototype tests are in the [preprint review](preprint-review.md).
