# You Are My Sunshine

Plants don't have feet.  Yet they move towards the sun.  WOW!

![Plant turning to the light](../images/sunflower_to_sun.jpg)  


## The Art Behind the Sunshine
I am building Sunshine.  It is a plastic flower that uses photoresistors and servo motors to move its face towards the sun.

# Thanks to Those That Went Before
I am grateful for (and in awe of) the knowledge these folks shared:
- [Great Scott's YouTube Video: DIY Solar Tracker || How much solar energy can it save?](https://www.youtube.com/watch?v=_6QIutZfsFs)
- [fbuenonet's Thingiverse Mini Pan Tilt - Servo G9](https://www.thingiverse.com/thing:708819)
- [What is a Servo Motor and How it Works?](https://www.youtube.com/watch?v=ditS0a28Sko) (Not sure why it's called a servo motor versus positioning motor?)

I learned from and copied several of the techniques they showed in their video.

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
- What months should Sunshine be outside?

- How much energy will the solar panel provide?
- Will my small solar panel be enough to power the microcontroller + servo motors?  Since the action of this art piece is to follow the sun, I am not concerned with powering when there is no sun.  However, most of the year, there will not be A LOT of sun to begin with.

- Can I go directly from solar panel to powering the microcontroller or do I have to use a battery?
# Materials
Due to time constraints, I am focusing on using components I have or make me happy:
- Microcontroller: Adafruit's ItsyBitsy.  I love working with Adafruit's stuff.  They are great people with a great community.  They and the community are kind and inclusive.
- Scripting Language: CircuitPython. It is a far easier environment than Arduino.
- A [small solar panel](https://amzn.to/2OGzq2h) gathering dust in one of our closets.
- A [Samsung INR18650-25R battery](https://www.imrbatteries.com/content/samsung_25r_2.pdf) also gathering dust.


# Answers
## Placement of Photoresistors


*TBD*
## Months Sunshine Should be Outside
The best months have higher levels of solar radiation.  These are correlated to times when we are outside.
### Summary

Given my research on monthly Solar Radiation values in the Seattle area, Sunshine is to provide outdoor art goodness from April through September.  During this time, the average amount of solar radiation in the Seattle area is around 200  W/m<sup>2</sup>.
### More Info

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
# Explore / Familiarize
Here is where I'm documenting coding experiments to best understand aspects of the build electronics.
## The Microcontroller
I'm using an [ItsyBitsy from Adafruit](https://learn.adafruit.com/assets/55467) running [CircuitPython 6](https://circuitpython.org/).  

![itsybitsy pinout](../images/adafruit_products_pinouts_itsybitsy.jpg)
## Mark's Photoresistor + Servo Motor Experiment
Recreating to do a better job on my build and to recreate in CircuitPython.
## Wiring Diagram
### Servo Motor
Servo motors are used for precise (angular or linear) positioning.
- [Adafruit's Circuit Python Servo Motor Fritzing Diagram](https://learn.adafruit.com/assets/51929)

![Servo motor wiring diagram](../images/circuitpython_FeatherM0ExpressServo_bb.jpg)

From [Adafruit's Learning Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo):

*Connect the servo's brown or black ground wire to ground on the CircuitPython board.*

*Connect the servo's red power wire to 5V power, USB power is good for a servo or two. For more than that, you'll need an external battery pack. Do not use 3.3V for powering a servo!*

*Connect the servo's yellow or white signal wire to the control/data pin, in this case A1 or A2 but you can use any PWM-capable pin.*
## Test
Ran [Adafruit's code](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/CircuitPython_Essentials/CircuitPython_Servo.py) using the Mu editor.  Worked great.

![Circuit Python Servo test](../images/circuitpython_servo_test.jpeg)

I used the USB pin for 5V power to servo and A2 for servo input.  Exactly what the learning guide said to do.


### Photoresistor control of servo
*Stopped here for now*
As is typical, [Adafruit has a great write up on photoresistors](https://learn.adafruit.com/photocells):

*Photocells are basically a resistor that changes its resistive value (in ohms Ω) depending on how much light is shining onto the squiggly face. They are very low cost, easy to get in many sizes and specifications, but are very inaccurate. Each photocell sensor will act a little differently than the other, even if they are from the same batch. The variations can be really large, 50% or higher! For this reason, they shouldn't be used to try to determine precise light levels in lux or millicandela. Instead, you can expect to only be able to determine basic light changes.*

Since the photoresistor is just a variable resistor, wiring and reading values uses a voltage divider as shown in [Adafruit's Learn page](https://learn.adafruit.com/photocells/using-a-photocell):

![photo resistor voltage divider](../images/light_cdsanasch.gif)

*The easiest way to measure a resistive sensor is to connect one end to Power and the other to a pull-down resistor to ground. Then the point between the fixed pulldown resistor and the variable photocell resistor is connected to the analog input of a microcontroller*

[Adafruit's wiring diagram](https://learn.adafruit.com/assets/49000):


![photo resistor wiring diagram](../images/light_m0_photocell_bb.png)

- Board 3.3V to one leg of the photocell (doesn't matter which leg).  Note you want to use the voltage from your board that corresponds to the maximum analog input voltage.  For Feather boards this is 3.3V, but for other boards it might be higher or lower--consult your board documentation to be sure.
- 10 kilo-ohm resistor to the other leg of the photocell.
- Board GND to the other leg of the 10 kilo-ohm resistor.
- Board A1 (or any other analog input) to the junction of the photocell & 10 kilo-ohm resistor.

*BELOW IS TBD...UNDER CONSTRUCTION*

# Stuff that I find Interesting
Learnings that help me be a better Maker.
## How Much Energy Will the Solar Panel Provide?
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

## How much Power Do We Need
The:
- microcontroller
- servo motors
Need power to operate.  How much?
## Microcontroller Power consumption





# Battery
I have a [Samsung INR18650-25R battery](https://www.imrbatteries.com/content/samsung_25r_2.pdf) that I am not using.


