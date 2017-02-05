# Stubs for pyspark.rddsampler (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class RDDSamplerBase:
    def __init__(self, withReplacement, seed: Optional[Any] = ...) -> None: ...
    def initRandomGenerator(self, split): ...
    def getUniformSample(self): ...
    def getPoissonSample(self, mean): ...
    def func(self, split, iterator): ...

class RDDSampler(RDDSamplerBase):
    def __init__(self, withReplacement, fraction, seed: Optional[Any] = ...) -> None: ...
    def func(self, split, iterator): ...

class RDDRangeSampler(RDDSamplerBase):
    def __init__(self, lowerBound, upperBound, seed: Optional[Any] = ...) -> None: ...
    def func(self, split, iterator): ...

class RDDStratifiedSampler(RDDSamplerBase):
    def __init__(self, withReplacement, fractions, seed: Optional[Any] = ...) -> None: ...
    def func(self, split, iterator): ...