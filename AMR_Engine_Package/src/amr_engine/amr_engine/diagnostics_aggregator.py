"""Aggregates diagnostic_msgs/DiagnosticArray reports from every subsystem
package into the single robot-wide health view the state machine reacts to.
"""

from diagnostic_msgs.msg import DiagnosticStatus


class DiagnosticsAggregator:

    def __init__(self):
        self._latest_by_source: dict[str, object] = {}

    def update(self, source: str, diagnostic):
        self._latest_by_source[source] = diagnostic

    def has_active_fault(self) -> bool:

        for diagnostic in self._latest_by_source.values():

            for status in diagnostic.status:

                if status.level != DiagnosticStatus.OK:
                    return True

        return False