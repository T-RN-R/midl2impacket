import pathlib
from midlparser import parse_idl
from impacketbuilder import ImpacketBuilder
from os import walk
import traceback
def generate_impacket(midl_def, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def generate(in_file, out_file, import_dir):
    print(f"Parsing {in_file}")
    in_file = pathlib.Path(in_file)
    if not in_file.exists():
        raise Exception(f"Provided input file {in_file} does not exist.")
    
    if not out_file:
        out_file = in_file.with_suffix('.impacket.py')
    out_file = pathlib.Path(out_file)

    midl_def = parse_idl(in_file)
    #print(midl_def)
    generated_code = generate_impacket(midl_def, import_dir)
    out_file.write_text(generated_code)

def test_full_pipeline():
    f = []
    for (dirpath, dirnames, filenames) in walk("./scraped"):
        f.extend(filenames)
        break
    print(f)
    failures = []
    for _f in f:
        try:
            generate("./scraped/"+_f, "./generated/"+_f.split(".")[0]+".py", "./scraped/")
        except:
            traceback.print_exc()
            failures.append(_f)
    print(f"Failed to parse: {failures}")


if __name__ == "__main__":
    test_full_pipeline()


        

