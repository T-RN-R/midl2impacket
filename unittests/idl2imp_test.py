import pathlib
from midlparser import parse_idl
from impacketbuilder import ImpacketBuilder

def generate_impacket(midl_def, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def test_full():
    scraped_files = pathlib.Path('preprocessed').glob("*.idl")
    for scraped_file in scraped_files:
        print(f"Parsing IDL {scraped_file}")
        midl = parse_idl(scraped_file)
        generate_impacket(midl, "./preprocessed/")


if __name__ == "__main__":
    test_full()


        

