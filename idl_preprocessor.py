import argparse
import pathlib
import shlex
import subprocess

class MidlPreprocessorException(Exception):
    pass

def preprocess_directory(input_dir:pathlib.Path, output_dir:pathlib.Path, pp_bin:pathlib.Path, pp_args:str):
    for idl_file in input_dir.glob("*.idl"):
        pp_cmd = f"{pp_bin.as_posix()} {pp_args} {idl_file.as_posix()}"
        print(pp_cmd)
        output_file = output_dir / idl_file.with_suffix('.preprocessed.idl').name
        pp_proc = subprocess.Popen(shlex.split(pp_cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = pp_proc.communicate()
        if not out:
            raise MidlPreprocessorException(f"Error processing {idl_file}: {out}")
        else:
            out_str = out.decode('utf-8')
            cur_lines = []
            for line in out_str.splitlines():
                if line := line.rstrip():
                    cur_lines.append(line)
            output_file.write_text('\n'.join(cur_lines))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pp', help='Path to IDL preprocessor e.g. "path/to/cl.exe" for MSVC', required=True)
    parser.add_argument('--args', help='Preprocessor arguments e.g. "/EP" for cl.exe', required=False, default='')
    parser.add_argument('--in-dir', help='Input IDL directory e.g. "scraped"', required=True)
    parser.add_argument('--out-dir', 
        help='Output directory e.g. "preprocessed". NOTE: If the preprocessor already writes to a file, \
              this directory will contain stdout for each invocation',
        required=True
    )

    args = parser.parse_args()
    input_dir = pathlib.Path(args.in_dir)
    if not input_dir.exists() or not input_dir.is_dir():
        raise MidlPreprocessorException(f"Provided input directory {args.in_dir} doesn't exist or isn't a directory!")
    
    output_dir = pathlib.Path(args.out_dir)
    output_dir.mkdir(exist_ok=True)

    pp_bin = pathlib.Path(args.pp)
    if not pp_bin.exists() and pp_bin.is_file():
        raise MidlPreprocessorException(f"Provided preprocessor doesn't exist or isn't a file!")
    
    preprocess_directory(input_dir, output_dir, pp_bin, args.args)



if __name__ == "__main__":
    main()