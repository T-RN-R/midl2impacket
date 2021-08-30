import argparse
import pathlib

import midltypes
from impacketbuilder import ImpacketBuilder
from fuzzer.template_generator import FuzzerTemplateGenerator
from midlparser import parse_idl


def generate_impacket(midl_def: midltypes.MidlDefinition, import_dir: str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def generate_template(midl_def: midltypes.MidlDefinition, import_dir: str):
    return FuzzerTemplateGenerator().generate(midl_def,import_dir)


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--in-file",
        "-in",
        type=str,
        help="IDL file to convert to Impacket",
        required=True,
    )
    parser.add_argument(
        "--out-file",
        "-out",
        type=str,
        help="Impacket output file",
        default=None,
        required=False,
    )
    parser.add_argument(
        "--import-dir",
        "-imp",
        type=str,
        help="IDL imports directory",
        default="./",
        required=False,
    )

    args = parser.parse_args()
    generate(in_file=args.in_file, out_file=args.out_file, import_dir=args.import_dir)


def generate(in_file, out_file, import_dir):
    print(f"Parsing {in_file}")
    in_file = pathlib.Path(in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {in_file} does not exist.")

    if not out_file:
        out_file = in_file.with_suffix(".impacket.py")
    out_file = pathlib.Path(out_file)
    
    midl_def = parse_idl(in_file)
    generated_code = generate_impacket(midl_def, import_dir)
    generated_template, uuid = generate_template(midl_def, import_dir)
    template_out = pathlib.Path(f"generated_fuzzers/{uuid}.py")
    template_out.write_text(generated_template)
    out_file.write_text(generated_code)


if __name__ == "__main__":
    main()
