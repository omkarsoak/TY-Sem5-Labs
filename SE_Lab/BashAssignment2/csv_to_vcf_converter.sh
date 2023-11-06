#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Error: File did not open"
    exit 1
fi

input_csv="$1"
output_vcf="output.vcf"

#checks for the number of columns and then makes vcard accordingly
#NR = number of records
#NF = number of fields

#awk -F',': Invokes AWK and sets the field separator as a comma.
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

