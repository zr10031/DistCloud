t = zeros(1,50);
for k = 1:50
	[~, t(k)] = Lab1_1(10e3,10);
	disp(t(k));
end

