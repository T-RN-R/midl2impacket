# MIDL2Impacket
MIDL2Impacket is a converter that takes a MIDL RPC definition and creates an Impacket RPC Python client. This project has 3 different components:

* A the actual MIDL to Impacket RPC converter `midl2impacket.py`
* An IDL scraper that pulls IDL files from MSDN `idl_scraper.py`
* An IDL preprocessor (requires MSVC) that applies macros to a given IDL file `idl_preprocessor.py`

## Usage

`python .\midl2impacket.py --in-file=[IDL FILENAME] --out-file=[PYTHON OUTPUT] --import-dir=[dir]`

Since some IDL files need to resolve imports, include the directory where it can find them.


## Known Issues
See TODOs in the code for more details
* String tokenization may be malformed if the string contains an escaped quotation mark
* Add an argument to lookup IDL imports inside of the Windows SDK

## Known Limitations
COM IDL definitons (specifically interface inheritance and library syntax) is not fully supported by the converter. They are technically supported by the parser, but the actual conversion of them to the Impacket format is a little bit iffy.