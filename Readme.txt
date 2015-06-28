==========================
README FILE - TAXI PROJECT
--------------------------
nmammo@uchicago.edu
slarrain@uchicago.edu
==========================

explore1.py:        Preliminary analysis

explore2.py:        Preliminary analysis

explore3.py:        Preliminary analysis

combine.py:         Combined the 2 files for each month into one.

rounder.py:         It round the GPS coordinates to the 3rd decimal.

point_polygon.py:   Check if a point is inside Manhattan.

cleaner.py:         Cleaned the Data.

randomizer2.py:     Randomly seleted 48k unique trips (4k for each month)

map_reduce3.py:     First MapReduce Job. Looks for similar trips from the random sample
                    Download file online - version.

map_reduce5.py:     First MapReduce Job. Looks for similar trips from the random sample
                    Reads file locally - version.

compare_datetimes.py:   evaluates whether two trips occurred at similar times of the day
                    and week.

analysis_within_similar_trips.py:   buckets each cluster of similar trips based
                    on time of day and then finds outlier trips that appear suspicious.

map_reduce6.py:     Second MapReduce Job. Finds every trip for the flagged drivers

map_reduce9.py:     Third and final MapReduce Job. Counts the number of times a flagged
                    driver was above 3 sd from the mean fare on all the trips he made.
                    Gives memory errors on AWS's EMR.
