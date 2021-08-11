import pathlib
from midlparser import parse_idl
from impacketbuilder import ImpacketBuilder

def generate_impacket(midl_def, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def test_full():
    scraped_files = pathlib.Path('scraped').glob("*.idl")
    for scraped_file in scraped_files:
        print(f"Parsing IDL {scraped_file}")
        midl = parse_idl(scraped_file)
        generated_code = generate_impacket(midl, "./scraped/")


if __name__ == "__main__":
    test_full()


        

