clear all
close all
clc

Body_Length = 18;

Rel_Bod_Len = 0:0.125:1;
Bod_Len_Adj = [0,.25,.45,.8,1,.8,.45,.25,0];
% Bod_Len_Adj = 0:0.125:1;
figure(1)
plot(Rel_Bod_Len,Bod_Len_Adj)

Wave_Length = [20,50,100,150,200,250,300];
Wave_Force = [30,14,7,6,5.5,5,4];
figure(2)
plot(Wave_Length,Wave_Force)

for i = 1:length(Wave_Force)
    Rel_Leng(i) = Body_Length/Wave_Length(i);
    Adj_Fact(i) = interp1(Bod_Len_Adj,Rel_Bod_Len,Rel_Leng(i));
    
end