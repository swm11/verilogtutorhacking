import marimo
import sys
sys.path.append("./")

app = marimo.App(width="medium")

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell
def left_menu():
    from common import mainmenu
    nav_menu = mo.sidebar(
        [
            mo.nav_menu(
                orientation = "vertical",
                menu = mainmenu()
                )
        ]
    )
    nav_menu
    return nav_menu

@app.cell
def _(mo):
    mo.md("# Traffic Light Example\n\n## Tutorial text\n\nModify the code below to see the impact on the simulation output.")
    return

@app.cell
def _(mo):
    global code_eg
    try:
        with open("dut_tlights_template.sv","r") as ftemplate:
            initial_code = ftemplate.read()
    except:
        initial_code = "ERROR: CODE TEMPLATE MISSING"
    editor = mo.ui.code_editor(value=initial_code, language="verilog")
    editor
    return editor, initial_code

@app.cell
def _(mo):
    simbutton = mo.ui.run_button(
        label="Run simulation",
    )
    simbutton
    return simbutton

@app.cell
def simulate(mo,editor,simbutton):
    import subprocess
    # don't run the simulation until the button has been pressed:
    mo.stop(not simbutton.value)
    with open("dut_tlights.sv","w") as f:
        f.write(editor.value)
    err = False
    verilog_out = "UNKNOWN ERROR"
    runrtn = subprocess.run(["verilator", "--binary", "-Wall", "tb_tlights.sv", "dut_tlights.sv"], capture_output=True, text=True, timeout=10)
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
        runrtn = subprocess.run(["./obj_dir/Vtb_tlights"], capture_output=True, text=True, timeout=10)
        if(runrtn.returncode!=0):
            verilog_out += f"command returned error code {runrtn.returncode}"
            err = True
        else:
            verilog_out = "<b>Simulation output:</b>\n"
            if(runrtn.stdout!=None):
                verilog_out += runrtn.stdout
            #if(runrtn.stderr!=None):
            #    verilog_out += runrtn.stderr
            verilog_out += "\n"
    return (verilog_out, )

@app.cell
def myout(mo, verilog_out):
    mo.md(verilog_out.replace("\n","<br>\n"))
    return

@app.cell
def _(mo):
    with open("tb_tlights.sv","r") as ftb:
        verilog = ftb.read()
    mo.md(f"## Test Bench Code\n```\n{verilog}\n```\n")
    

if __name__ == "__main__":
    app.run()
