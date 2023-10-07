# Regression-with-fixed-effects
Fixed effects is a method of controlling all variables, that stay constant within some larger category.

Shall issue laws in the 50 US states for 23 years will be analyzed in order to see if they reduce crime. These laws allow citizens to carry concealed weapons.
Proponents of these laws believe that this deters criminals from perpetrating violent crimes. Opponents argue that these laws may put more guns in circulation, leading to more crime and accidental use.
Here we run a regression on violent crime rate (incidents per 100,000 members of the population) using shall as an independent variable (1 if the state has a shall-carry law in effect in that year, =0 otherwise) and the covariates.

A state fixed effect for example will control for all unobserved factors that remain the same in a state over time and a year fixed effect will control for the aggregated shocks in a given year that affects all individuals equally.
The formula is Y_sy = BX_sy + a _s + g_y + e_sy. Being a_s the state fixed effect and g_y the year fixed effect.
By the results we cannot conclude that the laws either increased or decreased crime.
