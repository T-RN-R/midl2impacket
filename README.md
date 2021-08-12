# MIDL2Impacket
MIDL2Impacket is a converter that takes a MIDL RPC definition and creates an Impacket RPC Python client.

## Usage

`python .\midl2impacket.py --in-file=[IDL FILENAME] --out-file=[PYTHON OUTPUT] --import-dir`


## Known Issues
See TODOs in the code for more details
* String tokenization may be malformed if the string contains an escaped quotation mark