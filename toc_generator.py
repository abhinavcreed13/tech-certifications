'''
    Execute:
    python toc_generator.py --file="AZ-900 (Azure Fundamentals)\Udemy-Alan-Course-Notes\Section 2 - Azure Core Services - Azure Virtual Machines.md"
'''
import argparse
import md_toc

def get_args():
    """Argument parser.
    Returns:
      Dictionary of arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        type=str,
        help='file to be parsed')
    args, _ = parser.parse_known_args()
    return args

if __name__ == "__main__":
    # argument parser
    args = get_args()
    print(md_toc.build_toc(args.file), end='')