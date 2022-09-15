#!/usr/bin/env bash
# Convert FAVITES contact network to Cosmograph format (https://cosmograph.app/)
if [ "$#" -ne 2 ] ; then
    echo "USAGE: $0 <input_favites_contact_network> <output_cosmograph_file>"; exit 1
fi
echo "source,target" > "$2"
cat "$1" | grep "^EDGE	" | cut -f2,3 | tr '\t' ',' >> "$2"
