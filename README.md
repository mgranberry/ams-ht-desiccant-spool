# AMS-HT Desiccant Spool

A vented, rotating spool for drying indicator silica beads in the Bambu Lab AMS-HT. The design uses a one-piece drum with an integral sloped collector and pour spout, a bayonet fill lid, and bayonet plugs.

## Current files

- `print/ams-ht-drum-abs.3mf` — drum, sliced in Bambu Studio for ABS with supports disabled.
- `print/ams-ht-lid-and-plugs-abs.3mf` — removable lid and two plugs.
- `print/ams-ht-fit-coupons-abs.3mf` — fit coupons for the lid and port bayonets.
- `plans/` — geometry, render views, print review and validation notes.

The latest CAD assembly is available in [STEVE CAD](https://stevecad.studio/?document=f5b3f84b-33ae-484c-a498-2e649abe1053).

## Design overview

The spool is nominally 200 mm across the roller rim and 62 mm wide. Its cylindrical and end-face screens provide airflow, and internal fins lift the beads as the AMS-HT rotates the drum. A curved collector surface brings beads to an integral radial outlet. A straight nozzle lip fits into a receiving container. The removable fill lid and both port plugs use bayonet retention.

## Printing

The included 3MF plates were sliced in Bambu Studio 2.9.1 using the X1 Carbon 0.4 mm nozzle, Bambu ABS, 0.20 mm layers, and supports disabled. The two production plates use about 201 g of ABS including brims. Print the fit coupons first, then test lid retention and plug operation after an ABS heat cycle.

AMS-HT dimensions are 197–202 mm diameter and 50–68 mm width. The nominal spool envelope fits those dimensions.

## Validation status

CAD geometry builds successfully. Bambu Studio sliced the three included plates without supports or warnings. The bayonet paths, nozzle opening and 12 mm container-lip gauge were checked in CAD.

Physical bead retention, warm bayonet retention, roller runout, drainage and drying performance have not been validated. Test a partial load and check the actual target container before regular use.

See [the preprint review](plans/preprint-review.md) for detailed findings, measurements and acceptance checks.

## License

No license has been selected yet. All rights reserved unless a license file is added.
