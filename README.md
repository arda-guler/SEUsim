# SEUsim
Ever thought about how you would go about programming and operating a vulnerable computer under a high radiation environment?

**SEUsim is a Single Event Upset simulator** built to investigate the (potentially catastrophic) effects of Single Event Upsets on computer programs.

The simulation is built upon a [16-bit TurnaCore machine](https://github.com/arda-guler/TurnaCore), and the programs are written in AO, a custom assembly syntax for use with the TurnaCore instruction set (check the docs for more info!).

This repository can be thought of as a special branch of [TurnaCore](https://github.com/arda-guler/TurnaCore). See the [original repo](https://github.com/arda-guler/TurnaCore) for more information on using the machine or creating programs for it.

**The purpose of SEUsim is merely to flip random bits on the registers as a TurnaCore machine is running a program.**
