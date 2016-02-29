function [ MaxForce ] = Wave_Load( Body_Length,Displacement )
%UNTITLED2 Summary of this function goes here
%   Assumes 2.5' wave, finds maximum mooring force due to wave loading

Rel_Bod_Len = 0:0.125:1;
Bod_Len_Adj = [0,.25,.45,.8,1,.8,.45,.25,0];

Wave_Length = [20,30,40,50,100,150,200,250,300];
Wave_Force = [30,26,17,14,7,6,5.5,5,4];


for i = 1:length(Wave_Length)
    Rel_L(i) = Body_Length/Wave_Length(i);
    Adj_F(i) = interp1(Rel_Bod_Len,Bod_Len_Adj,Rel_L(i));
end

for i = 1:length(Wave_Length)
    Wave_L(i) = Body_Length/Adj_F(i);
    Wave_F(i) = interp1(Wave_Length,Wave_Force,Wave_L(i));
end

for i = 1:length(Wave_Length)
    Force(i) = Wave_F(i)*Displacement*Adj_F(i);
end
MaxForce = max(Force);

end

