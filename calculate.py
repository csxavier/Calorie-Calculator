 

 

#https://www.aqua-calc.com/calculate/daily-calorie-needs                        

#For men: 66 + (6.2 x weight) + (12.7 x height) – (6.76 x age)                       

#For women: 655.1 + (4.35 x weight) + (4.7 x height) – (4.7 x age)                             

 

#Points for activity levels are as follows:               

# 1.2 points for a person who does little to no exercise

# 1.37 points for a slightly active person who does light exercise 1–3 days a week

# 1.55 points for a moderately active person who performs moderate exercise 3–5 days a week

# 1.725 points for a very active person who exercises hard 6–7 days a week

# 1.9 points for an extra active person who either has a physically demanding job or has a particularly challenging exercise routine

 

#define Variables

 

Men_Constant_Value=66

Men_Weight_Constant=6.2

Men_Height_Constant=12.7

Men_Age_Constant=6.76

 

WoMen_Constant_Value=665.1

WoMen_Weight_Constant=4.35

WoMen_Height_Constant=4.7

WoMen_Age_Constant=4.7

 

Active_Activity_levels=[1.2,1.37,1.55,1.725,1.9]

 

def calculate_daily_calorie(Men_Or_WoMen,Weight,Height,Age,Active_Activity):

    if Men_Or_WoMen == "m" or  Men_Or_WoMen == "M":

        Constant_Value=Men_Constant_Value;

        Weight_Constant=Men_Weight_Constant;

        Height_Constant=Men_Height_Constant;

        Age_Constant=Men_Age_Constant;

    elif Men_Or_WoMen == "f" or  Men_Or_WoMen == "F":

        Constant_Value=WoMen_Constant_Value;

        Weight_Constant=WoMen_Weight_Constant;

        Height_Constant=WoMen_Height_Constant;

        Age_Constant=WoMen_Age_Constant;

    else:

        print ("Invalid Option for Men_Or_WoMen : ",Men_Or_WoMen)

   

    daily_calorie_needs=(Active_Activity * (Constant_Value +

                                        ((Weight_Constant * Weight) +

                                        (Height_Constant * Height)) -

                                        (Age_Constant * Age)

                                        )

                    );

    return round(daily_calorie_needs,2);

 

 

Men_Or_WoMen=input("Enter Men (m) or Women (f) : ");

print(Men_Or_WoMen);

 

Weight=float(input("Enter Weight (In Pounds) : "));

print(Weight);

 

Height=float(input("Enter Height (In Inches) : "));

print(Height);

 

Age=float(input("Enter Age (In Years) : "));

print(Age);

 

print("for a person who does little to no exercise) = 1.2");

print("for a slightly active person who does light exercise 1–3 days a week =  1.37");

print("for a moderately active person who performs moderate exercise 3–5 days a week = 1.55");

print("for a very active person who exercises hard 6–7 days a week = 1.725");

print("for an extra active person who either has a physically demanding job or has a particularly challenging exercise routine = 1.9");

Active_Activity=float(input("Enter Active Activity Level based on above : "));

print(Active_Activity);

 

daily_calorie_needs=0

 

print("Daily Calorie Needs :", calculate_daily_calorie(Men_Or_WoMen,Weight,Height,Age,Active_Activity));

 

 

 
