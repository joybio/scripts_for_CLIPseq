#!/bin/bash
macs2 callpeak --nomodel --shift 15 --extsize 30 -m 2 100 -t IP_18_OE-2.sorted.bam -c control_6_Col0-2.sorted.bam -f BAM -n OE-1.Col0 -p 0.01 -g 1.0e8 &

macs2 callpeak --nomodel --shift 15 --extsize 30 -m 2 100 -t IP_7_OE-1.sorted.bam -c control_5_Col0-1.sorted.bam -f BAM -n OE-2.Col0 -p 0.01 -g 1.0e8 &
















