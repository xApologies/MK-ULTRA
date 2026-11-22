import argparse
from .fixtures import demo_modules
from .brane import Brane
def main():
    p=argparse.ArgumentParser();p.add_argument('--demo',action='store_true');p.add_argument('--subject',default='time shell');p.add_argument('--output',default='./artifacts');a=p.parse_args()
    if not a.demo:p.error('reference CLI currently requires --demo')
    r=Brane(demo_modules(),a.output).handle({'operation':'generate_report','subject':a.subject});print(r.to_json())
if __name__=='__main__':main()
