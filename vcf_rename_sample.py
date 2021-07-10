import vcf
import argparse
import random

parser = argparse.ArgumentParser(description='convert vcf file')
parser.add_argument('--sample_size', type=int, nargs='?',
                    help='sample size for snp')
parser.add_argument('--count_snp', type=int, nargs='?', default=9751961,
                    help='All count for snp')

parser.add_argument('--input', type=str, nargs='?',
                    help='input file')

parser.add_argument('--output', type=str, nargs='?',
                    help='output file')

parser.add_argument('--convert', action='store_false')
args = parser.parse_args()

input_file = args.input
output_file = args.output
convert = args.convert

vcf_reader = vcf.Reader(open(input_file, 'r'))
vcf_writer = vcf.Writer(open(output_file, 'w'), vcf_reader)

#python convertor.py --sample_size=1000 --count
if __name__ == "__main__":
    sample_size = args.sample_size
    count = args.count_snp
    snp_samples = random.sample(range(count), sample_size)

    for id, record in enumerate(vcf_reader):
        if id in snp_samples:
            if convert:
                record.ID = str(record.CHROM) + "_"+ str(record.POS)
            vcf_writer.write_record(record)
    vcf_writer.close()