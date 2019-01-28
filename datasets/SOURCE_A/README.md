# SOURCE_A

- `SOURCE_A` is a relatively small sample of offline, and online signatures
- Assume the former (offline) is in an image format, while the latter (online) is an ASCII format with `X, Y, Z` (coordinates in float) per line
- For the purpose of this exercise, the files in the offline datasets are intentionally blank (no parsing needed), while the files in the online datasets are faked, and _may be invalid (requires parsing)_
- In both the offline, and offline sets, there are subsets of genuine, and forged signatures
- The datasets are incomplete: we do not have all the samples


## File Naming / Directory Convention

_NOTE: `*` is a wildcard for any file extensions, e.g. `PNG` or `HWR` in this context._

**Genuine Datasets**

Format: `<ID of Signee>_<Index of Signature / Sample Number>.*`
Examples:

- 001_01.png => Signee's unique ID is 1, and this is the first sample from the signee
- 001_02.png => Signee's unique ID is 1, and this is the second sample from the signee

The signee's unique ID is only unique to the specific directory that it is in.

**Forged Datasets**

Format: `<First 4 characters: ID of Forger><Next 3 characters: ID of Original / Reference Signee>_<Index of Signature / Sample Number>.*`
Examples:

- 0120001_1.HWR => Forger's unique ID is 120, original / reference signee's unique ID is 1, and this is the first sample from the forger
- 0120002_1.HWR => Forger's unique ID is 120, original / reference signee's unique ID is 2, and this is the first sample from the forger

The forger's unique ID is only unique to the specific directory that it is in. The original / reference signee's unique ID should exist in the genuine dataset. e.g. `0120001_1.HWR` is a forged version of a signature by the signee of `001_01.png`.
