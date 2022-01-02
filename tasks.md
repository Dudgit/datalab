1. Download a GTFS status of the BKK from <https://bkk.hu/apps/gtfs/> this database changes almost on a daily basis, so include in your report the time you obtained it. (You don't have to keep it up to date.)

2. Load those tables to your database that are relevant in creating a network between the routes. Which are these? If any tables need some preprocessing/cleaning you should do it before this task in the environment of your choice.

3. Create the link list of the transport routes! You can use the environment of your choice to calculate permutations if you don't want to do it in SQL.

4. Visualize the network you've obtained! Nodes with more links should be bigger, color the nodes according to what kind of transport they're: black for nighttime, yellow for trams, blue for busses etc. and label them what route they're. What seem to be the most well connected nodes in this network? How can you fix this? (<https://networkx.org/)>

5. Calculate the degree distribution and the average degree of the >fixed< network. Visualize the results! What does the shape of the distribution tell you about this particular network? (<http://networksciencebook.com/chapter/2#degree)>

6. Calculate the clustering coefficient for each node, from that obtain the average clustering, and also calculate the global clustering coefficient! Visualize the results! How does the distribution look like? How does the average clustering compare to the global clustering? (<http://networksciencebook.com/chapter/2#clustering>; <http://networksciencebook.com/chapter/2#advanced)>

7. Measure degree correlation function of the network! Visualize the results! What does this tell you about the assortativity of the network? (<http://networksciencebook.com/chapter/7#measuring-degree)>