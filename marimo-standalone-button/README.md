# Notes

## Purpose

Simple stand-alone test of Marimo running a simple web page allowing
Verilog to be entered and simulated.

Try using a button to ask the user when to rebuild the verilog and run
the simulation.

## To Run

To install:
* Install Verilator and Python3
* In a Python venv: `pip3 install marimo`

To run use:
```
marimo run standalone-marimo.py
```

This should open a page in your browser and present some initial code
and then run the simulator.  Every time the code is changed the
simulator is run.
