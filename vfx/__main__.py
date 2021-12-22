import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description='vfx contains video fx tools')
parser.add_argument('input', type=Path, help='path to input video or image to be processed')
args = parser.parse_args()

