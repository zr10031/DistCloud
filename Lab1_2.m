function [d,t] = Lab1_2(np, nd, nw)
% parallel
% use following code
% 
% d = zeros(1e7, 3);
% for k=1:3, [d(:,k), t(k)] = Lab1_2(1e7,1,k); end

if (nargin < 1), np = 1e5; nd = 10; nw=4; end
hp = gcp('nocreate');
if isempty(hp), hp=parpool(nw); end

A = randn(np, nd); B = randn(np, nd);
d = zeros(np, 1);
tic;
parfor i = 1:np
    for j = 1:nd
        d(i) = d(i) + (B(i,j)-A(i,j)).^2;
    end
    d(i) = sqrt(d(i));
end
t = toc;
delete(hp);