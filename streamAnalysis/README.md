# Tech Choice:
The Panda library in Python was used to explore the dataset. It is used to open the csv dataset and get statistical information.


# Approach to Exploration
Time was spent designing a program to calculate mean, standard deviations, max and min values, and various other statistics as well as analyzing the relationships between multiple columns of data. 

Then analysis was conducted to find the relationship with the data and any anomalies that there might be within the dataset.




# Data-driven recommendations

## Investigation and Repair recommended on Iron compatibility (good fraction of Iron browser users does not use p2p despite being connected to streamroot)
 
While analyzing the relationship between the connected column with the  browser and isp, I have noticed that a fraction of the p2p values were close to zero despite the user being connected to streamroot network (connected = true). For whatever, the data streaming uses only cdn and no p2p during download transmission at the time. 

In comparison to all browsers in all of the streams, the browser “Iron” seem to be the one to not use p2p despite being connected to streamroot (dominating stream 1, 2, 4, 5, and 8). Even Earthworm, a widely used browser in the dataset, seems to fall in comparison Iron in most streams, making the need for investigation and repair for Iron compatibility more urgent. (Note: For some reason, there was a spike of browser use that is connected with zero p2p for Vectrice).

**Please refer to the images in the "connect_p2p_zero" folder for reference.**

An inspection and repair is recommended on to why Iron refuses to get support from p2p, using most of cdn to download content despite being connected to the streamroot network.




## More focus on persuasion / investigation for Datch Telecam to connect to streamroot
I analyzed the relationship between the isp and connected values and noticed that Datch Telecam is the only isp that has a higher false connected than true across multiple streams.

This suggests that users of Datch Telecam are either avoiding or cannot connect to streamroot. 

More persuasion efforts to connect to streamroot / investigation on the failure of Datch Telecam to connect to streamroot is recommended.

## More p2p optimization recommended for Vectrice & Swamp
I noticed that the values of p2p while being connected to streamroot is quite low. 

However, this simply could be a result of the lack of Swamp and Vectrice users and that there usually isn’t two members using those browsers who are watching the same video at the same time.

## More p2p optimization recommended for Olga
I noticed that the values of p2p while being connected to streamroot is quite low. 

However, this simply could be a result of the lack of Olga users and that there usually isn’t two members using those service providers who are watching the same video at the same time.







# If there was more time
If there was more time, I would have experimented with unsupervised learning algorithms such as clustering or regression models to investigate the relationship of the data features even further.

