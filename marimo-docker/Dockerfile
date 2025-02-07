# syntax=docker/dockerfile:1.4

# Choose a python version that you know works with your application
FROM python:3.11-slim
# Install Verilator for Verilog simulations
run apt update
run apt install -y verilator

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.4.20 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Copy requirements file
COPY --link requirements.txt .

# Install the requirements using uv
RUN uv pip install -r requirements.txt

# Install Verilator and dependancies
RUN apt-get install -y build-essential verilator

# Copy application files
COPY --link app.py .
#COPY --link dut_template.sv .
#COPY --link testbench.sv .

EXPOSE 8080

# Create a non-root user and switch to it
RUN useradd -m app_user
USER app_user

WORKDIR /user_files
CMD [ "marimo", "run", "/app/app.py", "--host", "0.0.0.0", "-p", "8080" ]


