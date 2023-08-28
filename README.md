# SeparateMetabolomics
# Language: Python
# Input: TXT
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5

Separate abundance into groups

Input is a TXT file of keyword-value pairs (tab-delimited):

abundance_file: Path to CSV file of abundances
metadata: Metadata file (TXT)

Output will be multiple group files, using the user-specified prefix
