import pathlib
from midlparser import parse_idl

def test_full():
    scraped_files = pathlib.Path('scraped').glob("*.idl")
    for scraped_file in scraped_files:
        print(f"Parsing IDL {scraped_file}")
        midl = parse_idl(scraped_file)



        
