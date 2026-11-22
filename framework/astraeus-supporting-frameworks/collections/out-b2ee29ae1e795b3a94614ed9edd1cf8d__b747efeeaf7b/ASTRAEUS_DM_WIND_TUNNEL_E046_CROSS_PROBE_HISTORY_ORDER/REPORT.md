# ASTRAEUS Dark-Matter Wind Tunnel E046
## Cross-Probe History Order

**Naive response-strength ordering:** FAIL / parked  
**Saturation-distance ordering:** PASS across all 7 H/O views  
**Physical dark matter:** NOT YET

A simple idea failed first:

`History depth -> larger response magnitude`

is not exactly monotone. Every readout overshoots slightly before settling.

So I did not force that scalar.

The geometry-first replacement works.

For each probe view:

`delta_A(k) = ||R_A(E_k)-R_A(E16)|| / ||R_A(E0)-R_A(E16)||`.

For all seven independent Hydrogen/Oxygen views:

`delta_A(k+1) <= delta_A(k)`

over the entire tested orbit.

So History carries a robust **order of approach to the saturated basin**, even though
the absolute response magnitude is not monotonic.

This also explains the E044/E045 result cleanly:

- substrate topography stabilizes at `E6`;
- every H/O readout topography is stable by `E7`;
- exact states continue contracting inside that already-stable topographic basin.

## Next

Stop adding new History.

Test whether the saturated ER state persists or relaxes away under the most
source-valid no-new-write/read-only evolution available.

That is directly relevant to whether this is retained substrate memory or merely a
continuously driven transient.
