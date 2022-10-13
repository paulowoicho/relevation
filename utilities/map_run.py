import argparse
import Path
import json

parser = argparse.ArgumentParser(description='Re map a run file')
parser.add_argument('run_file', type=str)

args = parser.parse_args()

run_file_stem = Path(args.run_file).stem

with open('mapping.json') as query_mapping_file:
    query_mapping = json.load(query_mapping_file)


with open(f"{run_file_stem}_mapped.run", "w") as updated_run:
    with open(args.run_file) as original_run:
        for line in original_run:
            qid, Q0, docid, rank, score, run_name = line.split("\t")
            updated_run.write(f'{query_mapping[qid]}\t{Q0}\t{docid}\t{rank}\t{score}\t{run_name}')