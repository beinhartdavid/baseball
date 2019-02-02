# baseball

**Introduction:**

I'm convinced Alex Rodriguez had a sixth sense for hitting useless homeruns. Growing up a Yankees fan it seemed he had a knack for solo shots late in otherwise desolate games against the Red Soxs or to pile on in blow outs against the Orioles. 
But these hunches are just lost in the wash of negative feelings against the beleagered slugger. To quantify my claims I've turned to the cold hard truth: MLB Box Scores. 

**Setup:**


Ok box scores are pretty dense. I started by looking at https://www.baseball-reference.com/boxes/ but with so much information on EVERY play in a baseball game it seemed to be a bit much for my current needs. Luckily I found http://www.thebaseballgauge.com/ where I could filter out all play types, pulling up a table of just homeruns. 

With selenium and openpyxl I was able to assemble 25 years of homerun data into a spreadsheet. 

My next step is to load the information into Google BigQuery and conduct analysis. While I have been using the Query function in Google Sheets recently, the volume of data is too large for Google Sheets to keep up. 

**Defining "Overrated" Homeruns**

To conduct this analysis we'll need some definitions. What is an overrated homerun anyway?

One metric to use is WPA, a change in Win Probablity based on the outcome of a given play. Hitting a walkoff homerun has a pretty high WPA, 0.999 when relevent example or 0.000 when relevent example. 

