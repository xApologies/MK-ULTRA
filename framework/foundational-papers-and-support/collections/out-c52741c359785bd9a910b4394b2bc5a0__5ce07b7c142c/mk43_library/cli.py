import argparse,json
from .library import MK43Library
def main():
 p=argparse.ArgumentParser();p.add_argument("--db",required=True);p.add_argument("operation",choices=["recover"]);p.add_argument("handle");a=p.parse_args();l=MK43Library(a.db);print(json.dumps(l.export_address(a.handle),indent=2))
if __name__=="__main__":main()
