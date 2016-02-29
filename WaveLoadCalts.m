clear all
close all
clc

Body_Length = 18;

Rel_Bod_Len = linspace(0,1,0.125);
Bod_Len_Adj = [0,.3,.75,,1,.75,.3,0];
figure(1)
plot(Rel_Body_Len,Bod_Len_Adj)
