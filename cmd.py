#!/usr/bin/env python3

from ml_predict import process_cmd
import argparse

#./cmd.py -i inputfile -0 outputfile

if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Process gene file and output probability PDF")

    # Add the input and output file arguments
    parser.add_argument("-i", "--input", help="Input gene file path", required=True)
    parser.add_argument("-o", "--output", help="Output probability PDF file path", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the process_gene_file function with the provided input and output file paths
    process_cmd(args.input,args.output)
