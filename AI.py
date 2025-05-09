from google import genai





client = genai.Client(api_key="AIzaSyAOxHRPqBZAic_asutpVyVysZtT1QIhfDg")
print("      This is Personal AI designed By Mohammad Hoosain")
while True:
    
    print("-----------------------------Personal AI (Desinged by Mohammed Hussain)-------------------------------")
    query=input("Enter your query :")
    if query=="break" or query=="exit" or query=="stop":
        print("ok...you can call me anytime")
        print("ok...you can call me anytime")
        break
    else:
        print("loading....")
        print("\tYour Query :",query,"\n ")
        response = client.models.generate_content(
            
            model="gemini-2.0-flash",
            contents=query,
        )
        
        print("-----------------------------Answer From AI-------------------------------","\n\n ",response.text)
        printk(response.text)


