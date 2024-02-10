clear,clc
%Function1
[K, Ksubm, Qsubm] = func1;
%Function2
[d] = func2(Ksubm, Qsubm);
%Function3
[nodes,elements]=func3;
%Function 4
func4(nodes,d,elements)
%Function 5
Q_full=func5(K,d);
%Task 1
function [K, Ksubm, Qsubm] = func1
    K = readmatrix("K_matrix.csv");
    Ksubm = readmatrix("K_submatrix.csv");
    Qsubm = readmatrix("Q_subvector.csv");
end
%task 2.
function [d] = func2(Ksubm, Qsubm)
   
    d = inv(Ksubm) * Qsubm;
    d = [0; 0; d(1:10); 0; 0; d(11)];
end
%Function 3
function [nodes,elements] =func3
nodes=[0 0;0 21;35 26.5;70 21;70 0];
elements=[1 2;2 3;3 4;4 5];
for i=1:4
    plot(nodes(i:i+1,1),nodes(i:i+1,2),"k--.","MarkerSize",30)
   
    hold on
    xlim([-10 80])
    ylim([-10 36.5])
end
end
%Function 4
function func4(nodes,d,elements)
for i=1:5
    newnodes(i,1)=nodes(i,1)+d((3*i-2));
    newnodes(i,2)=nodes(i,2)+d((3*i-1));
end
title("Deformation of Structure With an Applied Force")
xlabel("Width (meters)")
ylabel("Height (meters)")
daspect([1 1 1])
plot_deformed_members(nodes,elements,d)
for i=1:5
    plot(newnodes(i,1),newnodes(i,2),"r","MarkerSize",30,"MarkerFaceColor","r","Marker",".")
end
hold off
end
%Function 5
function Q_full=func5(K,d)
%Solving full Q
Q_full=(K*d)./1000;
fprintf("At joint one the force experienced in the x direction is %.2f kN and in the y direction %.2fkN.\n",Q_full(1),Q_full(2))
fprintf("At joint five the force experienced in the x direction is %.2f kN and in the y direction %.2fkN.\n",Q_full(13),Q_full(14))
end