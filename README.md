# Evx predictor mlbot

This is a simple package used to generate buy and sell signals for crypto and conventional stock markets based on the excess volume indicator(EVX)  
You can read more about Evx in the whitepaper [here](https://www.researchgate.net/publication/345313655_DeFiPaper)

# Usage

In your python script simply import the module and use as follows  
from evxpredictor.mlbot import Evx

print(Evx.buySignalGenerator(20,65,120, 0.98))

Evx is the class and buysignalGenerator and sellSignalGenerator are methods in it.  
The above methods take an assets opening, closing, and volume of the asset based on the time interval you have chosen,  
while the last variable is alpha, a probabilistic value.


