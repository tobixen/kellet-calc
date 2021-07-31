# kellet-calc

When anchoring with a light-weight rope (instead of a chain), some boaters tend to add a heavy weight (kellet) on the anchoring rope.  I suppose it's an endless discussion on all boating forums, are kellets actually useful for other purposes than giving the captain a "warm and fuzzy feeling"?  Peter Smith, the designer of the Rocna anchor, says "no" - see https://www.petersmith.net.nz/boat-anchors/catenary.php and https://www.petersmith.net.nz/boat-anchors/kellets.php - but then again, most boaters I know of does not usually anchor up in 60 knots of wind.  For one thing, I do believe kellets may make sense in calm conditions on a dense anchorage with lots of other boats anchored with chain, and then I'm trying to anchor up in the middle of those ships using just a rope.

I know for sure that a kellet has great practical usage when doing a typical Oslofjord/Bohuslän stern anchoring with a rope from the bow to land in calm conditions.  It's nice to make the anchoring so that if pulling very hard on the ropes, one can make the distance from the bow to land short enough to allow people to easily get off and on, while the boat naturally will glide back and stay in a comfortable distance from land if giving the ropes some meters of slack.

I didn't find any formulas for the effect of a kellet easily available on the internet (for catenary for anchor chains and power cables there are lots of ready-to-use formulas on the internet though), so I decided to do some math and find the formulas.

This project was born out from a Norwegian boating forum, so as for now the input variables to the function is in Norwegian.  I will maybe and eventually remake it or make an english wrapper function, as well as add some of the information from the Norwegian forum into this README.  Here is some background information:

* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment-2315646
* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment=2316268
* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment=2316832
