1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

File "data/phase2.txt" seems to be the most active because it had the highest maximum heart rate (117) which falls in between the 95-162 heartrate range. However, most of the values still fall belowe the range allowing me to assume the participants weren't really active. The median and average for the data are also really close to each other allowing me to further assume the participants engaged in low activity. 

2) Which file had the **poorest** data quality? How do you know?

Phase 2 has the poorest data because it has the biggest outlier and the largest range as well. Higher ranges mean outliers are affecting the overall range and possibily the average.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
The range for this data set is 112.


b) Explain how the extreme value affects the range.
With out the extreme value the range is only 7, which a significant decrease from the range being 112.


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

I think the IQR would be a better statistic to represent the variability of this dataset because it is measure based on just the middle 50% of the data. In this data the middle 50% are closer in values making it a more reliable range.


