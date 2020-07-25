from typing import List


class CmdParserResult:
    def __init__(self, cmd: str = "", args: List[str] = None):
        self.cmd = cmd
        if args is None:
            args = []
        self.args = args
