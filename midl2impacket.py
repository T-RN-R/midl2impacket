import argparse
import logging
import midl
import impacket_generator
from midlparser import MidlParser

def parse(in_file) -> midl.MidlDefinition:
    logging.debug("Opening {in_file}")
    f = open(in_file, mode = 'r')
    data = f.read()
    f.close()
    if data is None:
        raise Exception(f"File `{in_file}` not found")
    p = MidlParser()
    return p.parse(data)

def generate_impacket(midl_def:midl.MidlDefinition):
    pass

def main():
    #TODO Once the Impacket generator is fully implemented, the commandline should accept --out_file arguments
    args = argparse.ArgumentParser(description='Process some integers.')
    args.add_argument('--in_file', type=str,
                        help='IDL file to convert to Impacket')
    arguments = args.parse_args()
    
    midl_def = parse(str(arguments.in_file))
    generate_code = generate_impacket(midl_def)
    #write to file...


if __name__ == "__main__":
    main()