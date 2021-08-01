# kellet-calc

When anchoring with a light-weight rope (instead of a chain), some boaters tend to add a heavy weight (kellet) on the anchoring rope.  I suppose it's an endless discussion on all boating forums, are kellets actually useful for other purposes than giving the captain a "warm and fuzzy feeling"?  Peter Smith, the designer of the Rocna anchor, says "no" - see https://www.petersmith.net.nz/boat-anchors/catenary.php and https://www.petersmith.net.nz/boat-anchors/kellets.php - but then again, most boaters I know of does not usually anchor up in 60 knots of wind.  For one thing, I do believe kellets may make sense in calm conditions on a dense anchorage with lots of other boats anchored with chain, and then I'm trying to anchor up in the middle of those ships using just a rope.

I know for sure that a kellet has great practical usage when doing a typical Oslofjord/Bohuslän stern anchoring with a rope from the bow to land in calm conditions.  It's nice to make the anchoring so that if pulling very hard on the ropes, one can make the distance from the bow to land short enough to allow people to easily get off and on, while the boat naturally will glide back and stay in a comfortable distance from land if giving the ropes some meters of slack.

I didn't find any formulas for the effect of a kellet easily available on the internet (for catenary for anchor chains and power cables there are lots of ready-to-use formulas on the internet though), so I decided to do some math and find the formulas.

This project was born out from a Norwegian boating forum, so as for now the input variables to the function is in Norwegian.  I will maybe and eventually remake it or make an english wrapper function, as well as add some of the information from the Norwegian forum into this README.  Here is some background information:

* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment=2315646
* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment=2316268
* https://baatplassen.no/i/topic/163530-p%C3%A5-svai-med-blytau/?do=findComment&comment=2316832

## Assumptions:

* Static state, no acceleration involved, steady wind.  This is hardly true, the wind changes direction all the time and comes in gusts, the boat is likely to be shaped in such a way that it will swing forth and back rather than staying steady against the wind.  The kellet will move up and down, and it will typically move up while the forces are greatest - hence, regarding the ropes angle of attack at the anchor, the kellet is likely to perform worse than what those calculations shows.
* Rope has the same weight as water (and the part that is above water should have the same weight as air).  That's not true, but an ordinary anchoring rope without a lead core is typically being close to the weight of water.  It's usually very visible that the rope has some weight when the wind is still, but the effect of the rope weight is insignificant when there is signifiant wind.
* Zero distance from the water surface to the connection point at the boat.  This is obviously not true, but if including the distance in the depth parameter then things should work out pretty well.
* Totally inelastic ropes.  This is obviously not true, but it shouldn't make any significant impact anyway - especially not when considering that everything is "steady state".
* The kellet weight already has the water displacement subtracted - so if the "kellet weight" is given as 10 kg, the mass of the kellet has to be above 10 kg.  This depends on the material used.  Consider a 25l plastic container filled with water - it's quite heavy, but obviously not suitable as a kellet - if there is any air bubble in it, it will likely float, and the kellet weight will be negative!  If steel is used (~8 times as dense as water), the kellet should be around 11.3 kg.
