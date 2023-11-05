#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Error: File did not open"
    exit 1
fi

input_csv="$1"
output_vcf="output.vcf"

#checks for the number of columns and then makes vcard accordingly

awk -F',' 'NR==1 {
    for (i=1; i<=NF; i++) {
        columns[i] = $i
    }
} NR>1 {
    # Print VCARD for each data row
    print "BEGIN:VCARD"
    for (i=1; i<=NF; i++) {
        printf "%s:%s\n", columns[i], $i
    }
    print "END:VCARD"
}' "$input_csv" > "$output_vcf"

echo "Conversion complete!"

