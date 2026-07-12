"""Siren + light GPIO drive. Kept dead simple so it works even if the
RPi-side amr_error logic is unavailable -- the watchdog calls into this
directly on heartbeat loss.
"""


class SignalIO:
    def __init__(self):
        # TODO: machine.Pin outputs for SIREN_PIN/LIGHT_PIN.
        pass

    def set(self, siren_on: bool, light_on: bool):
    # TODO: Implement siren/light GPIO control.
    # For now, do nothing instead of crashing.
      return