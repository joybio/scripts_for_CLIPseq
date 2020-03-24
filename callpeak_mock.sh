#!/bin/bash
macs2 callpeak --nomodel --shift 25 --extsize 50 -m 2 100 -t control_5_Col0-1.sorted.bam -c IP_7_OE-1.sorted.bam -f BAM -n negative_control/native-1.Col0 -p 0.01 -g 1.0e8 &

macs2 callpeak --nomodel --shift 25 --extsize 50 -m 2 100 -t control_6_Col0-2.sorted.bam -c IP_18_OE-2.sorted.bam -f BAM -n negative_control/native-2.Col0 -p 0.01 -g 1.0e8 &















