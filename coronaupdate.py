from covid import Covid 

covid = Covid() 
def worldcases():
    ch=""
    ch+="Worldwide report"
    confirmed = covid.get_total_confirmed_cases() 
    ch+='\nConfirmed :'+str(confirmed) 

    active = covid.get_total_active_cases() 
    ch+="\nActive:"+str(active)

    recovered = covid.get_total_recovered() 
    ch+='\nRecovered:'+str(recovered)

    deaths = covid.get_total_deaths() 
    ch+='\nDeaths:'+str(deaths)
    
    ch+="\n\n Enter the country you want to get data of :"
    return ch

def f():
    name=entry.get()
    details=countrycases(name)
    label=tk.Label(text=details)
    label.pack()
    
def countrycases(name_Country):
    ch=""
    country_cases = covid.get_status_by_country_name(name_Country)
    l=['country','confirmed','active','deaths','recovered']
    for x,y in country_cases.items():
        if(x in l):
            ch+=str(x)+':'+str(y)+"\n"
    return ch
    
import tkinter as tk
r=tk.Tk()
world=tk.Label(text=worldcases())
entry=tk.Entry()
button=tk.Button(r,text='Get Data',width='30',command=f)
world.pack()
entry.pack()
button.pack()
r.mainloop()


