import pathlib
from midlparser import parse_idl
from impacketbuilder import ImpacketBuilder
import traceback
from fuzzer.template_generator import FuzzerTemplateGenerator

def generate_impacket(midl_def, import_dir:str):
    return ImpacketBuilder().midl_def(midl_def).import_dir(import_dir).build()
def generate_template(midl_def, import_dir: str):
    return FuzzerTemplateGenerator().generate(midl_def,import_dir)


def test_full():
    generated_dir = pathlib.Path('generated')
    generated_dir.mkdir(exist_ok=True)
    scraped_files = pathlib.Path('preprocessed').glob("*.idl")
    #scraped_files = [pathlib.Path('preprocessed/ms-rprn.idl')]
    for scraped_file in scraped_files:
        out_file = generated_dir / scraped_file.with_suffix('.py').name
        print("Parsing: ", scraped_file)
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
        try:
            generated_template, uuid = generate_template(midl, "./preprocessed/")
            template_out = pathlib.Path(f"generated_fuzzers/{uuid}.py")
            template_out.write_text(generated_template)
        except Exception as ex:
            print(f"Unable to generate template for {scraped_file}: {ex}")
            traceback.print_exc()
            continue

if __name__ == "__main__":
    test_full()


        

