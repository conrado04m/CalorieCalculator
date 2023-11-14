import tkinter
from tkinter import ttk
from tkinter import messagebox

def calculate_height(feet, inches):
    heightInInches = (int(feet) * 12) + int(inches)
    heightInCm = heightInInches * 2.54
    return heightInCm

def calculate_weight(weight):
    return (round(float(weight) / 2.2046, 2))

def calculate_bmr(height, weight, gender, age):
    # Using Mifflin-St Jeor Equation
    if gender == "Male":
        bmr = round((10 * weight) + (6.25 * height) - (5 * int(age)) + 5)
    else:
        bmr = round((10 * weight) + (6.25 * height) - (5 * int(age)) - 161)
    return bmr

def calculate_tdee(bmr, workout):
    if workout == "Little/None":
        tdee = round(1.2 * bmr)
    elif workout == "1-3 times/week":
        tdee = round(1.375 * bmr)
    elif workout == "3-5 times/week":
        tdee = round(1.55 * bmr)
    elif workout == "6-7 times/week":
        tdee = round(1.725 * bmr)
    else:
        tdee = round(1.9 * bmr)
    return tdee

def display_results(tdee):
    # Calculations for weight loss
    maintain = tdee
    halfPerWeek = round(tdee - (1750 / 7))
    onePerWeek = round(tdee - (3500 / 7))
    twoPerWeek = round(tdee - (7000 / 7))
    
    # Create labels for type of weight loss
    maintainLabel = tkinter.Label(weightLossDisplayFrame, text="Maintain weight")
    halfLabel = tkinter.Label(weightLossDisplayFrame, text="0.5 lb/week")
    oneLabel = tkinter.Label(weightLossDisplayFrame, text="1 lb/week")
    twoLabel = tkinter.Label(weightLossDisplayFrame, text="2 lb/week")
    
    # Display type of weight loss labels
    maintainLabel.grid(row=0, column=0)
    halfLabel.grid(row=1, column=0)
    oneLabel.grid(row=2, column=0)
    twoLabel.grid(row=3, column=0)
    
    # Create labels for calories calculated
    maintainCalLable = tkinter.Label(weightLossDisplayFrame, text=str(maintain) + " Calories/day")
    halfCalLable = tkinter.Label(weightLossDisplayFrame, text=str(halfPerWeek) + " Calories/day")
    oneCalLable = tkinter.Label(weightLossDisplayFrame, text=str(onePerWeek) + " Calories/day")
    twoCalLable = tkinter.Label(weightLossDisplayFrame, text=str(twoPerWeek) + " Calories/day")
    
    # Display calories label
    maintainCalLable.grid(row=0, column=1)
    halfCalLable.grid(row=1, column=1)
    oneCalLable.grid(row=2, column=1)
    twoCalLable.grid(row=3, column=1)
    
    # Padding for widgets
    for widget in weightLossDisplayFrame.winfo_children():
        widget.grid_configure(padx= 25, pady=5)

def calculate_data():
    # User info
    age = ageSpinbox.get()
    heightFt = heightFtSpinbox.get()
    heightIn = heightInSpinbox.get()
    weight = weightSpinbox.get()
    gender = genderCombobox.get()
    workout = workoutCombobox.get()
    
    # Check for correct input
    if gender and workout:
        # Calculate data
        heightInCm = calculate_height(heightFt, heightIn)
        weightInKg = calculate_weight(weight)
        bmr = calculate_bmr(heightInCm, weightInKg, gender, age)
        tdee = calculate_tdee(bmr, workout)
        
        # Display results
        display_results(tdee)    
    else:
        tkinter.messagebox.showwarning(title="Error", message="Gender and activity are required.")

# Create window/root
root = tkinter.Tk()
root.title("Calorie Deficit Calculator")

# Create a frame to keep widgets in
frame = tkinter.Frame(root)
frame.pack()

# User info label frame
infoFrame = tkinter.LabelFrame(frame, text="User Information")
infoFrame.grid(row=0, column=0, padx=20, pady=10)

# Age widgets
ageLabel = tkinter.Label(infoFrame, text="Age")
ageSpinbox = tkinter.Spinbox(infoFrame, from_=15, to=110, width=5)

# Age widget alignment
ageLabel.grid(row=0, column=0)
ageSpinbox.grid(row=1, column=0)

# Height Widgets
heightLabel = tkinter.Label(infoFrame, text="Height(Ft, In)")
heightFtSpinbox = tkinter.Spinbox(infoFrame, from_=4, to=6, width=5)
heightInSpinbox = tkinter.Spinbox(infoFrame, from_=0, to=11, width=5)

# Height widget alignment
heightLabel.grid(row=0, column=1, columnspan=2)
heightFtSpinbox.grid(row=1, column=1)
heightInSpinbox.grid(row=1, column=2)

# Weight widgets
weightLabel = tkinter.Label(infoFrame, text="Weight")
weightSpinbox = tkinter.Spinbox(infoFrame, from_=110, to=400, increment=.1)

# Weight widget alignment
weightLabel.grid(row=0, column=3)
weightSpinbox.grid(row=1, column=3)

# Gender widgets
genderLabel = tkinter.Label(infoFrame, text="Gender")
genderCombobox = ttk.Combobox(infoFrame, values=["Male", "Female"])

genderLabel.grid(row=2, column=0)
genderCombobox.grid(row=3, column=0)

# Activity list
activityList = ["Little/None", "1-3 times/week", "3-5 times/week",
                "6-7 times/week", "Every day/physical job"]

# Workout Widgets
workoutLabel = tkinter.Label(infoFrame, text="Activity")
workoutCombobox = ttk.Combobox(infoFrame, values=[activityList[0], activityList[1], 
                               activityList[2], activityList[3], activityList[4]])

# Workout widget alignment
workoutLabel.grid(row=2, column=1, columnspan=2)
workoutCombobox.grid(row=3, column=1, columnspan=2)

# Padding for widgets in infoFrame
for widget in infoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# Weight loss display label frame
weightLossDisplayFrame = tkinter.LabelFrame(frame, text="Result")
weightLossDisplayFrame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Calculate button
calculateButton = tkinter.Button(frame, text="Calculate", command= calculate_data)

# Calculate button alignment
calculateButton.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Run program
root.mainloop()