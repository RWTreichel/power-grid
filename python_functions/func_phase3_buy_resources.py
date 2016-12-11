"""
Phase 3 - Buying Resources

In this phase, the players can buy resources for their power plants from the resource market. A player can only buy
resources for plants he owns. A plant cannot produce electricity unless it has enough resources to be fully powered.
This phase is played in reverse player order. The last player starts.

Every power plant can store twice as many resources as needed for production. Every power plant only stores the kind of
resource it uses for production (a coal power plant stores only coal, a hybrid power plant can store both coal and
oil, an ecological power plant never stores resources, etc). Each player can buy resources up to the maximum allowed in
 all his plants (twice as many as the production numbers of all his plants).

Changelog:
12/11/2016 - Created by Justin
"""
