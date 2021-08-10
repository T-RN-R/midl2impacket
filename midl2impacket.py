import argparse
import logging
import midl
import pathlib
from impacketbuilder import ImpacketBuilder
from midlparser import parse_idl

def generate_impacket(midl_def: midl.MidlDefinition, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def main():
    #TODO Once the Impacket generator is fully implemented, the commandline should accept --out_file arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--in-file', '-in', type=str, help='IDL file to convert to Impacket', required=True)
    parser.add_argument('--out-file', '-out', type=str, help='Impacket output file', default=None, required=False)
    parser.add_argument('--import-dir', '-imp', type=str, help='IDL imports directory', default="./", required=False)

    args = parser.parse_args()
    
    
    in_file = pathlib.Path(args.in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {args.in_file} does not exist.")
    
    if not args.out_file:
        args.out_file = in_file.with_suffix('.impacket.py')
    out_file = pathlib.Path(args.out_file)

    
    midl_def = parse_idl(in_file)
    #print(midl_def)
    generated_code = generate_impacket(midl_def, args.import_dir)
    out_file.write_text(generated_code)


if __name__ == "__main__":
    main()