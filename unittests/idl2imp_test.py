import pathlib
from midlparser import parse_idl
from impacketbuilder import ImpacketBuilder
import traceback

def generate_impacket(midl_def, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()

def test_full():
    generated_dir = pathlib.Path('generated')
    # scraped_files = pathlib.Path('preprocessed').glob("*.idl")
    scraped_files = [pathlib.Path('preprocessed/ms-rprn.idl')]
    for scraped_file in scraped_files:
        out_file = generated_dir / scraped_file.with_suffix('.py').name
        print("Parsing: ", out_file)
        try:
            midl = parse_idl(scraped_file)
        except Exception:
            print(f"Unable to parse file: {scraped_file}")
            continue
        try:
            generated_code = generate_impacket(midl, "./preprocessed/")
        except Exception as ex:
            print(f"Unable to generate impacket for {scraped_file}: {ex}")
            traceback.print_exc()
            continue
        out_file.write_text(generated_code)


if __name__ == "__main__":
    test_full()


        

