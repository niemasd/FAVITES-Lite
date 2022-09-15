#!/usr/bin/env bash
# Convert FAVITES transmission network to Cosmograph format (https://cosmograph.app/)
if [ "$#" -ne 2 ] ; then
    echo "USAGE: $0 <input_favites_transmission_network> <output_cosmograph_file>"; exit 1
fi
echo "time,source,target" > "$2"
cat "$1" | grep -v "^None	" | awk '{ print $3 ",\"" $1 "\",\"" $2 "\"" }' >> "$2"
