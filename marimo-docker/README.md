# Notes

## Purpose

Simple Docker-based test of Marimo running a simple web page allowing
Verilog to be entered and simulated.

## To Run

To build the docker container user script:
```
./docker.build
```

To run use script:
```
./docker.run
```

This should provide a web service at localhost:8080

Open your web browser localhost:8080 and you should see some initial code
and then run the simulator.  Every time the code is changed the
simulator is run.

## Current Limitations

Currently the starting verilog template (`dut_template.sv`), testbench
(`testbench.sv`) and the generated file containing the user's code
(`dut.sv`) are stored in the `user_files` directory bound to the
docker container as a read/write file system mounted as
`/userfiles`. Obviously for multi-user use, some sort of
authentication and user-file separation would be required.
