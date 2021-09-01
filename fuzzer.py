import argparse
import pathlib
from midlparser import parse_idl
import midltypes
from impacketbuilder import ImpacketBuilder
from fuzzer.core import Fuzzer


def generate_impacket(midl_def: midltypes.MidlDefinition, import_dir: str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

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
        "--out-dir",
        "-out",
        type=str,
        help="output directory",
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
    generate(args.idl, args.count, args.out_dir, args.import_dir)


def generate(in_file, count, out_dir, import_path):
    print(f"Parsing {in_file}")
    in_file = pathlib.Path(in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {in_file} does not exist.")
    out_path = out_dir
    pathlib.Path(out_path).mkdir(exist_ok=True)
    py_name = str(in_file).split("\\")[-1].replace(".idl", ".py")
    py_name = py_name.replace("-", "_")
    defintion = pathlib.Path(out_path + py_name)

    midl_def = parse_idl(in_file)
    generated_code = generate_impacket(midl_def, import_path)
    defintion.write_text(generated_code)
    # import the template to populate the fuzzing data structures
    defintion_import = str(defintion).replace("\\",".")[:-3]
    fuzzer = Fuzzer(count, defintion_import)
    fuzzer.run()



if __name__ == "__main__":
    main()
