import marimo

app = marimo.App(width="medium")

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _(mo):
    mo.md("# Example of Verilog Simulation\n\n## Tutorial text\n\nModify the code below to see the impact on the simulation output.")
    return

@app.cell
def _(mo):
    global code_eg
    initial_code = "CODE TEMPLATE MISSING"
    with open("dut_template.sv","r") as ftemplate:
        initial_code = ftemplate.read()
    editor = mo.ui.code_editor(value=initial_code, language="verilog")
    editor
    return editor, initial_code

@app.cell
def _(editor):
    import subprocess
    with open("dut.sv","w") as f:
        f.write(editor.value)
    err = False
    verilog_out = "UNKNOWN ERROR"
    runrtn = subprocess.run(["verilator", "--binary", "-Wall", "testbench.sv", "dut.sv"], capture_output=True, text=True, timeout=10)
    if(runrtn.returncode!=0):
        verilog_out="Compilation output:\n"
        if(runrtn.stderr!=None):
            verilog_out = runrtn.stderr
        verilog_out = f"{verilog_out}\nReturned error code {runrtn.returncode}"
        err = True
    else:
        verilog_out = "Compilation output:"
        if(runrtn.stdout!=None):
            verilog_out += runrtn.stdout
        if(runrtn.stderr!=None):
            verilog_out += runrtn.stderr
        verilog_out += "\n"
    if(not(err)):
        runrtn = subprocess.run(["./obj_dir/Vtestbench"], capture_output=True, text=True, timeout=10)
        if(runrtn.returncode!=0):
            verilog_out += f"command returned error code {runrtn.returncode}"
            err = True
        else:
            verilog_out = "Simulation output:\n"
            if(runrtn.stdout!=None):
                verilog_out += runrtn.stdout
            if(runrtn.stderr!=None):
                verilog_out += runrtn.stderr
            verilog_out += "\n"
    return (verilog_out, )

@app.cell
def myout(mo, verilog_out):
    mo.md(f"```\n{verilog_out}\n```\n")
    return

@app.cell
def _(mo):
    with open("testbench.sv","r") as ftb:
        verilog = ftb.read()
    mo.md(f"## Test Bench Code\n```\n{verilog}\n```\n")
    

if __name__ == "__main__":
    app.run()
