means = zeros(1,8);
for h = 1:8
	t = zeros(1,20);
	for i = 1:20
		[~,t(i)] = Lab1_2(10e3,10,h);
	end
	means(h) = sum(t) / 20;
end