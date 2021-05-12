# Advanced SIR Epidemic Modelling Program


This Repository can be used to simulate an epidemic using a system of ODEs which define the time rate
of change in the number of people in a given "state" (with respect to the epidemic).

This Repo allows two versions of a simulation to be used. 1st is a Basic simulator with 3 epidemic states
The 2nd is an advanced simulator with 8 Virus states.

They are both built upon the same principals of SIR modelling. 


User can select to use default parameters to define the simulation

or 

User can input all of the parameters themselves which are held to relevant conditions

The program can be used to also plot the results of the simulations on a graph and save the graph to a .png file.

The plots you want to see on the graph can be selected via a GUI ( please install easygui)

The parameters used to define the simulation can be saved to a .txt file 


-- USAGE--

The program is operated via the runsim.py file using command line arguments which are explained 
and defined in the runsim.py file.

In order to use the program please install easygui 









This Version Includes:

-----Basic SIR -----

(Susceptible, Infected, Recovered)

----States----

#Susceptible#

S

#Infected#

I

#Recovered Alive #

R


------- Constants/Coefficients ---------

Format:
	
	Description of Constants
    
    = variable name for use in functions
    
-------------------------------------------------------------

• Number of Contacts by an infected person per day which are Sufficient to spread the disease:

	 = beta
	 
• Recovery rate of Infected People. (I.e 1/number of days it takes to become noninfectious) :
  	
	= gamma
	



----- Advanced SIR -----

Susceptible, Exposed , Infected States - (Asymptomatic, Symptomatic, SelfIsolated, Hospitalised) 

Recovered Alive, Dead


----States----

#Susceptible#

S

#Exposed#

E

#Asymptomatic (Infected)#

Asymp

#Symptomatic (Infected)#

Symp

#Self Isolated#

Iso

#Hospitalised #

Hos

#Dead from Virus #

D

#Recovered Alive #

R

------- Constants/Coefficients ---------

Format:
	Description of Constants
    (Dictionary Key) = variable name for use in functions
    
-------------------------------------------------------------

Variables involved in Susceptible to exposed

( Contacts = contacts sufficient to spread virus):

	• Asymptomatic Number of Contacts per day
	    ("AsympC") = a
	• Symptomatic Number of Contacts per day
        ("SympC") = b
	• Isolated Number of contacts per day
        ("IsoC") = c
	• Hospitalized Number of contacts per day 
        ("HosC") = f
-------------------------------------------------------------
Exposed to Asymptomatic / Symptomatic :


	• Fraction of Exposed Population that become
        asymptomatic infected per day

           ("EAsymp") = g

	• Fraction of Exposed Population that become
        symptomatic infected per day

        ("ESymp") = j

	• Sum of g , j = Fraction of Exposed Population
        that become infected each day 

        =  k
-------------------------------------------------------------
Symptomatic to Isolation :

	• Fraction of Symptomatic Population that become isolated
	 per day

        ("SympIso") = L 
-------------------------------------------------------------
Isolation to Hospital :

	• Fraction of Isolated population that become hospitalized
	per day

	("IsoHos") = m
-------------------------------------------------------------
Hospital to Dead:

	• Fraction of Hospitalized population that die per day

	("HosD") = p
-------------------------------------------------------------
Recovery Constants 

	• Fraction of Asymptomatic Population that recover each day

	("AsympR") = q

	• Fraction of isolated population that recover each day

	("IsoR") = u

	• Fraction of Hospitalized Population that recover each day
	("HosR") = v
-------------------------------------------------------------

'''    
