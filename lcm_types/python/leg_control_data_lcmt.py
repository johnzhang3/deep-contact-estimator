"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class leg_control_data_lcmt(object):
    __slots__ = ["q", "qd", "p", "v", "tau_est"]

    __typenames__ = ["float", "float", "float", "float", "float"]

    __dimensions__ = [[14], [14], [6], [6], [12]]

    def __init__(self):
        self.q = [ 0.0 for dim0 in range(14) ]
        self.qd = [ 0.0 for dim0 in range(14) ]
        self.p = [ 0.0 for dim0 in range(6) ]
        self.v = [ 0.0 for dim0 in range(6) ]
        self.tau_est = [ 0.0 for dim0 in range(12) ]

    def encode(self):
        buf = BytesIO()
        buf.write(leg_control_data_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>14f', *self.q[:14]))
        buf.write(struct.pack('>14f', *self.qd[:14]))
        buf.write(struct.pack('>6f', *self.p[:6]))
        buf.write(struct.pack('>6f', *self.v[:6]))
        buf.write(struct.pack('>12f', *self.tau_est[:12]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != leg_control_data_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return leg_control_data_lcmt._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = leg_control_data_lcmt()
        self.q = struct.unpack('>14f', buf.read(56))
        self.qd = struct.unpack('>14f', buf.read(56))
        self.p = struct.unpack('>6f', buf.read(24))
        self.v = struct.unpack('>6f', buf.read(24))
        self.tau_est = struct.unpack('>12f', buf.read(48))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if leg_control_data_lcmt in parents: return 0
        tmphash = (0xe1630cd6417db1d9) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if leg_control_data_lcmt._packed_fingerprint is None:
            leg_control_data_lcmt._packed_fingerprint = struct.pack(">Q", leg_control_data_lcmt._get_hash_recursive([]))
        return leg_control_data_lcmt._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

