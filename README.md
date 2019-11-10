# inifinera_Escalation_prediction

# Overall Solution Process

Objective: when new query arrives, identify past queries that are "similar" and return the solutions which received high
positive feedback (along with Elastic Search results)

At query time, we will execute, two parallel queries - one to the Feedback object and the other to the Elastic Search.
We will Show Feedback object first and then the Elastic Search results below

At query time:

For the new query, identify the closest cluster

if distance to cluster is below threshold, and total feedback for the cluster is above the threshold:

return the top solutions ranked by aggregate feedback score, for queries in this group

Extension Logic: Find the set of clusters that are closer and do the aggregation of the solution objects and combine
them all

Show the feedback based results first and then the Elastic Search tradition results below

If an Object shows up on the Feedback (or identified as the incorrect solution), remove from showing on the bottom
Elastic Search results
