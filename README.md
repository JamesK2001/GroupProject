# GroupProject
Simulation of an epidemic using connected rates of change and ODEs.
A development on the SIR model to introduce more "states" that a populant
can be assigned wrt the virus.
This Version Includes:
Susceptible , Exposed , Infected States - (Asymptomatic, Symptomatic, Self
Isolated, Hospitalised) , Recovered Alive, Dead
Calculating the connected rates of change using a transition flow diagram
(In Research Documents) and associated constants / coefficients which
define the rate at which these transitions occur. An array of these coefficients
associated with the National (UK) and Local (Bristol) COVID-19 outbreak
will be available for users to input into the simulation program.
The DEs are integrated over the 'duration' of the simulation and
currently :
plotted with a minimum 1 day time step intervals and solved using initial conditions provided
by default or provided by the user.
should:
export the array of data to be used by other functions
These initial conditions take the form State0 Where State is replaced with
the corresponding shorthand State ID as shown below
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
