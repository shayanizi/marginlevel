#!/usr/bin/python3.8.0
class CalculateB:
    def __init__(self,rate_ex,lot_ex,lev_ex):
        self.rate_ex=rate_ex
        self.lot_ex=lot_ex
        self.lev_ex=lev_ex
    def margin_ex(self):
        return (self.rate_ex*self.lot_ex*100000)/(self.lev_ex)
    def freemargin_ex(self):
        return ((self.margin_ex())*(0.1))
    def marginlevel_ex(self):
        return (self.freemargin_ex()/self.margin_ex())
    def equity_ex(self):
        return (self.margin_ex()+self.freemargin_ex())
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
import_ex=CalculateB(
    float(input("How much rate?! ")),
    float(input("How much lot?! ")),
    int(input("How much leverage?! "))
)
margin=CalculateB.margin_ex(import_ex)
print("Your margin is >>",margin)
freemargin=CalculateB.freemargin_ex(import_ex)
print("Your freemargin is >>",freemargin)
equity=CalculateB.equity_ex(import_ex)
print("Your equity is >>",equity)