"""Backwards compatibility module for lttbc-offsets.

With this module, users will be able to use lttbc.downsample() exactly like they
always did (not expecting the third offsets array), whereas users who need the
offsets can use `lttbc_offsets.downsample`.

The former simply calls the latter, but discards the offsets array before
returning.
"""

from lttbc_offsets import downsample as downsample_offsets

def downsample(x, y, threshold):
    """Compatibility thunk for pre-offsets lttbc"""
    nx, ny, _ = downsample_offsets(x, y, threshold)
    return nx, ny
