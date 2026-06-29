"""Thin executable entry point. The actual supervisor logic lives in
state_machine_node.py -- this file just exists to be the literal
"AMR Engine" the user runs/launches.
"""
from amr_engine.state_machine_node import main

if __name__ == '__main__':
    main()
