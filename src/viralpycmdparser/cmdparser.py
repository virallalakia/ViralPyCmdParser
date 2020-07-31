import re

from viralpycmdparser.result.cmdparserresult import CmdParserResult


class CmdParser:
    def __init__(self, delim=" "):
        self.delim = delim

    def parse(self, cmd_str: str) -> CmdParserResult:
        result = CmdParserResult()
        if cmd_str:
            cmd_str = re.sub(self.delim + "{2,}", self.delim, cmd_str)
            t = cmd_str.strip(self.delim).split(self.delim)
            result.cmd = t[0]
            if len(t) > 1:
                result.args = t[1:]
        return result
