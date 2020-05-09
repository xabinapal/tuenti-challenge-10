#!/usr/bin/env sh

function file_to_hex {
    local path="${1}"
    dc -e "10o 16i $(od -An -tx1 "${path}" | tr -d ' \n' | tr '[[:lower:]]' '[[:upper:]]') p"  | tr -d '\\\n'
}

extract_dir=$(mktemp -d)
unzip ../assets/challenge-12/testdata.zip -d "${extract_dir}" > /dev/null

cat <<EOF
m1 = $(file_to_hex "${extract_dir}/plaintexts/test1.txt")
c1 = $(file_to_hex "${extract_dir}/ciphered/test1.txt")

m2 = $(file_to_hex "${extract_dir}/plaintexts/test2.txt")
c2 = $(file_to_hex "${extract_dir}/ciphered/test2.txt")

e = 65537

m1e = m1^e
m1ec1 = m1e -c1
m2e = m2^e
m2ec2 = m2e - c2
n = GCD[m1ec1, m2ec2]

BitLength[n]
EOF

rm -rf "${extract_dir}"