import argparse, json
from .library import TransductionLibrary

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--db",required=True)
    sp=p.add_subparsers(dest="cmd",required=True)
    a=sp.add_parser("recover"); a.add_argument("handle")
    a=sp.add_parser("model"); a.add_argument("model_handle")
    a=sp.add_parser("search"); a.add_argument("text")
    args=p.parse_args()
    lib=TransductionLibrary(args.db)
    if args.cmd=="recover": out=lib.export_address(args.handle)
    elif args.cmd=="model": out=lib.recover_model(args.model_handle)
    else: out=lib.search(args.text)
    print(json.dumps(out,indent=2,ensure_ascii=False))
    lib.close()

if __name__=="__main__": main()
