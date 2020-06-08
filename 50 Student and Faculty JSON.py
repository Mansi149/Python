"""
PROBLEM 50
Write a program to print the output of the following poblem statement :-
Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )?
"""
# use jsonlindt to run this code 
[
{
    "College_Student": 
        {
    		"firstName": "Mansi",
			"lastName": "Pareek",
			"user_Id": "pareek_mansi",
			"Depatment": "CSE",
			"Contact_Details": 
    			{
    				"phoneNumber": 
        				{
        					"num1": "+91 7936926938",
        					"num2": "+91 7936926898"
        				},
    				"email_id": "pareekmansi@gmail.com"
    			}
		}
},
{
	"College_Faculty": 
    	{
			"firstName": "Ruchika",
			"lastName": "Khandewal",
			"user_Id": "khandelwal_ruchika1",
			"Research_area": "none",
			"Depatment": "CSE",
			"Contact_Details": 
    			{
    				"phoneNumber": 
        				{
        					"num1": "+91 7936926938",
        					"num2": "+91 7936926898"
        				},
    				"email_id": "khruchika@gmail.com"
    			}
		}
},
{
	"College_Faculty": 
    	{
			"firstName": "Sarbhjeet",
			"lastName": "Singh",
			"user_Id": "singh_sarbhjeet2",
			"Research_area": "microprocessors",
			"Depatment": "EE",
			"Contact_Details": 
    			{
    				"phoneNumber": "+91 7567926938",
    				"email_id": "sisarbhjeet@gmail.com"
    			}
		}
}
] 
