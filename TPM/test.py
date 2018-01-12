import ctypes


class Tspi:
    def __init__(self):
        self.hContext = ctypes.c_uint32(0)
        self.tspi = ctypes.CDLL('libtspi.so.1')
        e = self.tspi.Tspi_Context_Create(ctypes.pointer(self.hContext))
        assert e==0,'Error: %x' % e

    def err(self,e):
        nr = '0x%03x' % (e & 0xfff)
        m = [x for x in open('/usr/include/tss/tss_error.h').read().split('\r') if nr.upper() in x.upper()][0].strip()
        m=m.split()[1]
        return 'Tspi Error 0x%03x %s, from /usr/include/tss/tss_error.h' % (e & 0xfff, m)

    def Context_Connect(self):
        e = self.tspi.Tspi_Context_Connect(self.hContext, None)
        assert e==0,self.err(e)
        return self

    def GetTpmObject(self):
        self.hTPM = ctypes.c_uint32(0)
        e = self.tspi.Tspi_Context_GetTpmObject(self.hContext, ctypes.pointer(self.hTPM))
        assert e==0,self.err(e)
        return self

    def PcrRead(self, nr):
        pcrLength = ctypes.c_uint32(0)
        pcrValue = ctypes.POINTER(ctypes.c_ubyte)()
        e = self.tspi.Tspi_TPM_PcrRead(self.hTPM, nr, ctypes.pointer(pcrLength), ctypes.pointer(pcrValue))
        assert e==0,self.err(e)
        return pcrValue[0:pcrLength.value]


def TPM():
    t = Tspi()
    return t.Context_Connect().GetTpmObject()


tpm = TPM()
print(tpm.PcrRead(5))
