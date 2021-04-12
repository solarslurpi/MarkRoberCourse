# You Are My Sunshine

I find it fascinating - spiritually moving even 0 that while plants don't have feet, they do position themselves in the best possible light.

![Plant turning to the light](../images/sunflower_to_sun.jpg)  

I am building Sunshine.  It is a plastic flower that moves its flower face towards the sun.


A plant's movement towards light is referred to as [phototropism](https://en.wikipedia.org/wiki/Phototropism).

For my electronics art project, I will be building a plastic sunflower that uses:
- [photoresistors](https://amzn.to/325qMO6) to sense where the most sunlight is coming from.
- [server motors](https://amzn.to/3a0HVwN) to move the sunflower to a position that maximizes the amount of light hitting it.
- [a solar panel]()

# Requirements
E = Essential
NE = Non-Essential
In priority order
- E Simplify the project such that it is completed within the 3 day timeframe.
- E Flower (head) moves it's face to the sun.
- E Powered by a battery so it can be outside.
- NE Solar panel recharges battery.  I mean, we're in the sun, go solar!


- NE Flower also has a stem that moves (gracefully) when the flower moves.  It is easiest to make just the head and have it move.  Mounting the head on a long stem and then adjusting the stem provides an "eye catcher".  However, the weight of the flower on the stem causes a challenge as does mimicking graceful movement.  With that said it is an opportunity to combine mechanical with electrical....

TL;DR Sadly, not enough time for putting a stem on.

- E powered by solar.  I mean, this is all about honoring the sun's power!

# Questions
- Where should I place the photoresistors to maximize the effect of head movement?
- How much energy will the solar panel provide?
- Will my small solar panel be enough to power the microcontroller + servo motors?  Since the action of this art piece is to follow the sun, I am not concerned with powering when there is no sun.  However, most of the year, there will not be A LOT of sun to begin with.

- Can I go directly from solar panel to powering the microcontroller or do I have to use a battery?

- Given the amount of solar radiation, are there limitations to which months Sunshine should be working?

# How much Power Do We Need
The:
- microcontroller
- servo motors
Need power to operate.  How much?
## Microcontroller Power consumption

## What Months are Best?
The best months have higher levels of solar radiation.  These are correlated to times when we are outside.
## Summary

Given my research on monthly Solar Radiation values in the Seattle area, Sunshine is to provide outdoor art goodness from April through September.  During this time, the average amount of solar radiation in the Seattle area is around 200  W/m<sup>2</sup>.

## More Info

I found a [University of Washington website](http://www.weatherjon.org/meteo/pages/station/climate.php?var=S) that provides average monthly solar radiation values for Seattle.  I downloaded as a csv file than used a [CSV to Markdown table generator](https://donatstudios.com/CsvToMarkdownTable) to get to the table below


| ""          | "Avg" | "Min" | "Max"  | "Range" | 
|-------------|-------|-------|--------|---------| 
| "January"   | "36"  | "0"   | "587"  | "587"   | 
| "February"  | "68"  | "0"   | "777"  | "777"   | 
| "March"     | "111" | "0"   | "1021" | "1021"  | 
| "April"     | "167" | "0"   | "1181" | "1181"  | 
| "May"       | "207" | "0"   | "1253" | "1253"  | 
| "June"      | "228" | "0"   | "1355" | "1355"  | 
| "July"      | "248" | "0"   | "1241" | "1241"  | 
| "August"    | "213" | "0"   | "1120" | "1120"  | 
| "September" | "150" | "0"   | "1132" | "1132"  | 
| "October"   | "82"  | "0"   | "970"  | "970"   | 
| "November"  | "43"  | "0"   | "709"  | "709"   | 
| "December"  | "29"  | "0"   | "480"  | "480"   | 

The values are in W/m<sup>2</sup>.

**Looking at the numbers, Sunshine will be doing its thing during the months of April through September.**

Averaging out these average values (167+207+228+248+213+150)/6 = 202 W/m<sup>2</sup>
 
# How Much Energy Will the Solar Panel Provide?
I have [a small solar panel](https://amzn.to/2OGzq2h).  I am using this one instead of spending more time on research because of the project's time constraint.

The Amazon page notes:
- 5V
- 30mA
- 53x30mm

Usually, specifications are made during times when solar radiation is at its peak wherever these panels are manufactured.  *Maybe* we'll get close to these values in July...

If the panel works to these specifications:
```
P = IV
P = .03A * 5V = .15W
```
Our tiny solar cell won't have much solar harvesting, but if we're careful with how we use the battery, we'll  be able to extend battery recharging times.
# Battery
I have a [Samsung INR18650-25R battery](https://www.imrbatteries.com/content/samsung_25r_2.pdf) that I am not using.


