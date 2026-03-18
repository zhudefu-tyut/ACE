import os
import sys
import pathlib

rhino8_sys = pathlib.Path(r"D:\Rhino 8\System")
assert rhino8_sys.exists(), "cuo"
sys.path.insert(0, str(rhino8_sys))
os.environ["PATH"] = str(rhino8_sys) + os.pathsep + os.environ.get("PATH", "")

import rhinoinside
rhinoinside.load()
import Rhino
from Rhino.FileIO import FileStpWriteOptions


STP_IN  = r"D:\Work_Directory_new\model-repair.stp"
STP_OUT = r"D:\Work_Directory_new\model-repair-AP214.stp"

def stp_214(src: str, dst: str):
    doc = Rhino.RhinoDoc.CreateHeadless(None)
    try:
        if not doc.Import(src):
            raise RuntimeError("STP cuo")

        opt = FileStpWriteOptions()
        opt.Scheme = 214

        if not Rhino.FileIO.FileStp.Write(dst, doc, opt):
            raise RuntimeError("STP cuo")
        print("done", dst)
    finally:
        doc.Dispose()

if __name__ == "__main__":
    stp_214(STP_IN, STP_OUT)