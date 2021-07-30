# MIDL2Impacket
MIDL2Impacket is a converter that takes a MIDL RPC definition and creates an Impacket RPC Python client.

## Usage

`python .\midl2impacket.py --in_file=[IDL FILENAME]`


## Known Issues
See TODOs in the code for more details
* Does not parse MIDL procedures yet
* Unions are not handled properly, they are just treated as inline structs.
* The parsed IDL is not converted into an Impacket RPC implementation
* GUIDs may be treated as numbers if they start with a digit, which will cause unhandled errors
* String tokenization may be malformed if the string contains an escaped quotation mark
* Minor nit: Currently many internal `midl.py` structs are exposed to the parser. Some of parsed structs are added via an `add_*` function in `midl.py`, hiding away the internal struct (`MidlDefinition.add_import`). Other calls expect the interal `midl.py` struct to already be created(`MidlDefition.add_interface`). Fix this to be consistent across all of `midl.py`.
* Minor nit: Separate UUID and Version parsing into a MIDLInterfaceHeader class, away from MidlInterface