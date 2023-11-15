# Calorie Deficit Calculator with Python

## An easy to use graphical user interface for users to input their information to learn about caloric deficits.

This project was built to help those who are trying to understand their caloric intake and how to possibly lose or maintain their weight.

## How to use this program.

The user must do the following:

* Input their age with a starting point of 15.
* Input their height which consists of two separate inputs. User must first input their height in feet, then their height in inches.
* Input their weight with a starting point of 110 pounds. User can input decimals for exact weight.
* Input their gender using a combobox with the options of male and female.
* Input their activity level using a combobox ranging from no activity to activity every day.

## How I calculated the caloric deficit.

First I needed to calculate the user's BMR (basal metobolic rate) which is essentially the bodies bare minimum necessity in order to function. I calculated this using the user's weight, age, and height.

Afterwards I calculated the users TDEE (total daily energy expenditure). This is the total amount of energy a person uses in a day. This can very wildy depending on many different factors, one of which being the user's activity rate. This is taken into account by asking the user their thoughts on how they view their activity. Using the calculated BMR and user's activity level I was able to calculate their TDEE.

Finally, using the TDEE I was able to calculate the total caloric intake per-day necessary for the four options provided. Essentially a pound of fat is 3500 calories. Taking this into account in order to maintain weight that would simply be the users calculated TDEE. If the user wanted to lose half a pound per week we can take 3500 and divide it by 2. Then we can divide this by 7 essentially getting how much a half pound would be per day. Then subtract the TDEE by this amount. Now I have the amount a person would need to eat per day in order to lose a half of a pound per week. Repeat this process for a pound which would be the full 3500 divided by 7 or 2 pounds per week which would be 7000 divided by 7.

## Deeper insight as to why I chose certain options.

I chose the starting point for age to be 15 because people under the age of 15 will likely not be looking to lose weight. This application would not be appropriate for those under the age of 15 due to possible health concerns. After doing research it can be become dangerous to eat under a certain amount of calories per day and calculations at such a young age often conflict with this issue.

Similarly, I chose the starting point for weight to be 110 pounds. This application would not be necessary for someone under the weight of 110 pounds and further weight loss could be harmful.