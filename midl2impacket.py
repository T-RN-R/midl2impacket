import argparse
import logging
import midl
import pathlib
from impacketbuilder import ImpacketBuilder
from midlparser import MidlParser

def parse(in_file: pathlib.Path) -> midl.MidlDefinition:
    logging.debug(f"Opening {in_file}")
    data = in_file.read_text()
    if not data:
        raise Exception(f"File `{in_file}` is empty")
    p = MidlParser()
    return p.parse(data)

def generate_impacket(midl_def: midl.MidlDefinition):
    return ImpacketBuilder().midl_def(midl_def).build()

def main():
    #TODO Once the Impacket generator is fully implemented, the commandline should accept --out_file arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--in-file', '-in', type=str, help='IDL file to convert to Impacket', required=True)
    parser.add_argument('--out-file', '-out', type=str, help='Impacket output file', default=None, required=False)
    args = parser.parse_args()
    
    in_file = pathlib.Path(args.in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {args.in_file} does not exist.")
    
    if not args.out_file:
        args.out_file = in_file.with_suffix('.impacket.py')
    out_file = pathlib.Path(args.out_file)

    midl_def = parse(in_file)
    generated_code = generate_impacket(midl_def)
    out_file.write_text(generated_code)


if __name__ == "__main__":
    main()