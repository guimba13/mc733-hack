perf stat -r 3 -d -e cycles,branches,branch-misses,cpu-clock,cache-references,cache-misses python benchmark.py 2> perf.txt

python output.py perf.txt

