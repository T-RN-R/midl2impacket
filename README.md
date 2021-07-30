# MIDL2Impacket
MIDL2Impacket is a converter that takes a MIDL RPC definition and creates an Impacket RPC Python client.

## Usage

`python .\midl2impacket.py --in_file=[IDL FILENAME]`


## Known Issues
* Does not generate procedure functions yet
* unions are not handled properly, they are just treated as inline structs.
* The parsed IDL is not converted into an Impacket RPC implementation
* GUIDs may be treated as numbers if they start with a digit, which will cause unhandled errors
