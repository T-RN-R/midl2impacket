import argparse
import pathlib
from midlparser import parse_idl
import midltypes
from impacketbuilder import ImpacketBuilder
from fuzzer.template_generator import FuzzerTemplateGenerator
from fuzzer.core import Fuzzer


def generate_impacket(midl_def: midltypes.MidlDefinition, import_dir: str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()


def generate_template(midl_def: midltypes.MidlDefinition, import_dir: str):
    return FuzzerTemplateGenerator().generate(midl_def, import_dir)


def main():
    parser = argparse.ArgumentParser(description="Fuzz an RPC server")
    parser.add_argument(
        "--idl",
        "-u",
        type=str,
        help="IDL file of server to target",
        required=True,
    )
    parser.add_argument(
        "--name",
        "-n",
        type=str,
        help="server name",
        required=True,
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        help="number of testcases to generate",
        default=1,
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
    generate(args.idl, args.count, args.name, args.import_dir)


def generate(in_file, count, servername, import_path):
    print(f"Parsing {in_file}")
    in_file = pathlib.Path(in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {in_file} does not exist.")
    out_path = "out/" + servername + "/"
    pathlib.Path(out_path).mkdir(exist_ok=True)
    template = pathlib.Path(out_path + "template.py")
    server = pathlib.Path(out_path + "server.py")

    midl_def = parse_idl(in_file)
    generated_code = generate_impacket(midl_def, import_path)
    generated_template, uuid = generate_template(midl_def, import_path)
    template.write_text(generated_template)
    server.write_text(generated_code)
    # import the template to populate the fuzzing data structures
    __import__(str(template).replace("\\",".")[:-3])
    for i in range(0, count):
        fuzzer = Fuzzer(str(server).replace("\\",".")[:-3], str(template).replace("\\",".")[:-3])
        fuzzer.fuzz_one()
        fuzzer.clear_state()


if __name__ == "__main__":
    main()
