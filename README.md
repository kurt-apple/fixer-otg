# fixer-otg
- Fork of [ChrisChrisLoLo/pusheenz40](https://github.com/ChrisChrisLoLo/pusheenz40). Also gathered info from [idawgz32](https://github.com/ChrisChrisLoLo/idawgz32) and [bunchiez40](https://github.com/ChrisChrisLoLo/bunchiez40).
- Layout is all-new, and design emphasizes ultra portable, small form factor while still having a fairly sane key map.
- Blog posts hosted on [Obsidian Publish](https://publish.obsidian.md/kurt/Maps/Fixer+OTG).
- FAK Firmware is [here!](https://github.com/kurt-apple/fak)

# Keyboard Design
As a parent, I often find myself "nap-trapped" but still needing to do computer work. After trying several Android touchscreen keyboards I have concluded that my fingers are not up for the task anymore. However, I still require a handheld form factor. More recently I spotted the uConsole from ClockworkPi and while it looks neat, I reason that if I have to wait many months to receive one, I might as well challenge myself to DIY. What could go wrong? 

The intent is to use these schematics (bunchiez40, pusheenz40, and idawgz32) as a launching-off point for an ambitious, DIY pocket keyboard, which will later evolve into a "deck" or "pocket" pc. Some requirements are currently listed in the [TODOs](TODO.md).

# Status
- prototype keyboard PCBs were ordered and will arrive Aug 23
- A rough-draft custom layout for the oddly shaped keyboard is done; Lots of fine-tuning to do.
- I've got my eyes set on a few display modules and I am interested in designing a CM4 carrier or picking another small SBC to dedicate to the project.

# Navigating the KiCad Files
I used a plugin called "Hierarchical-PCB" which allowed me to define a subcircuit in separate `kicad_pcb` files, then copy the layout specified in that `kicad_pcb` file whenever a hierarchical sheet of the same name is placed in the schematic of another PCB.

> [!Warning]
> "Hierarchical-PCB" does not yet support nested hierarchical sheets. I forked the project and I want to try to add this support at a later date. Nevertheless, this plugin was VERY helpful in both making the schematic visually less noisy and also in quickly laying out tedious portions of the keyboard PCB.

To open the design I am using currently, please open the main `kicad_pcb` file titled `fixer-otg.kicad_pcb`.

# Making One
- DM me on Discord (@present_day) to check if I have any boards remaining
- Get yourself some Kailh Mute Micro Switches (42x)
- Fork my FAK repo for the firmware code, and modify however much you wish.
- Gather your soldering supplies
- My provided manufacturing files (gerber, drilling, BOM) are specifically for JLCPCB. If you want to print them at a different company you might have to output your own manufacturing files.
- All but the switches are PCBA.
- Receive your board(s)
- Recommended: flash firmware and short out each key by hand to make sure the keys work
- Solder the mute switches to each pad
- Test it out

# BOM
This is the BOM. Note that most PCB prototype services have a minimum order quantity of around 5.
|  Comment | | CPCB Part # | QTY | Price 5 Boards |
|---|---|---|---|
| USB C Port | C165948 | 5 | $0.779 |
| CH552T | C111367 | 5 | $2.543 |
|   |   |   |   |
